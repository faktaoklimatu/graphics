#!/usr/bin/env python3
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
import logging
from pathlib import Path
import re
from subprocess import run, PIPE
import sys
from typing import Dict, List, Optional


IGNORED_COMMIT_RE = re.compile(r'^\s*\[(skip|ignore)\]\s*$',
                               re.IGNORECASE | re.MULTILINE)
VERSION_OVERRIDE_RE = re.compile(r'^\s*\[version\s*=([^\]]+)\]\s*$',
                                 re.IGNORECASE | re.MULTILINE)
CLEANUP_RE = re.compile(r'\n*\s*\[(skip|ignore|version\s*=[^\]]+)\]\s*\n+',
                        re.IGNORECASE)


@dataclass
class Commit:
    sha1: str
    author_date: datetime
    message: str
    body: Optional[str] = None
    _files: List[Path] = field(default_factory=list, init=False)
    _skip_flag: Optional[bool] = field(default=None, init=False)
    _version: Optional[str] = field(default=None, init=False)

    @classmethod
    def parse_from_log(cls, text: str) -> 'Commit':
        first_line, body = text.split('\n', 1)

        # Parse basic properties from first line.
        sha1, timestamp, message = first_line.split(' ', 2)
        author_date = datetime.fromtimestamp(int(timestamp))
        commit = cls(sha1, author_date, message)

        # Store the commit message body if present.
        if body:
            commit.body = body

        return commit

    @property
    def clean_body(self) -> Optional[str]:
        if not self.has_body:
            return None
        assert isinstance(self.body, str)

        return CLEANUP_RE.sub('\n', self.body)

    @property
    def files(self) -> List[Path]:
        return self._files

    def _generate_version_from_date(self) -> str:
        return self.author_date.strftime('%Y-%m-%d')

    @property
    def has_body(self) -> bool:
        return self.body is not None

    @property
    def has_skip_flag(self) -> bool:
        if self._skip_flag is None:
            self._skip_flag = (self.has_body and
                               IGNORED_COMMIT_RE.search(self.body) is not None)

        return self._skip_flag

    def parse_file_list(self, git_output: str) -> None:
        for line in git_output.split('\n')[:-1]:
            _, filename = line.split('\t', 1)
            self._files.append(Path(filename))

    def _parse_version_override(self) -> Optional[str]:
        if not self.has_body:
            return None
        assert isinstance(self.body, str)

        match = VERSION_OVERRIDE_RE.search(self.body)

        return match[1].strip() if match else None

    @property
    def version(self) -> str:
        if self._version is None:
            self._version = self._parse_version_override()

        if self._version is None:
            self._version = self._generate_version_from_date()

        assert isinstance(self._version, str)

        return self._version


def make_github_blob_url(repository: str, commit: Commit, path: Path) -> str:
    return f'https://github.com/{repository}/blob/{commit.sha1}/{path}'


if __name__ == '__main__':
    github_repository = sys.argv[1] if len(sys.argv) > 1 else 'faktaoklimatu/graphics'

    logging.basicConfig(format='[%(levelname)s] %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger()

    git_log_output = sys.stdin.read()
    if not git_log_output:
        sys.exit(0)

    changelogs: Dict[Path, str] = defaultdict(str)

    git_log_lines = git_log_output.split('\0')
    num_commits = len(git_log_lines)
    for i, log_entry in enumerate(git_log_lines):
        commit = Commit.parse_from_log(log_entry)
        logger.info('[%2d/%2d] Parsed commit %s authored %s', i + 1, num_commits,
                    commit.sha1, commit.author_date)

        if not commit.has_body:
            logger.info('Skipping due to empty body')
            continue

        if commit.has_skip_flag:
            logger.info('Skipping due to flag')
            continue

        # Ask git which files were changed (A-added or M-modified) in
        # the commit.
        cmd = run(['/usr/bin/git', 'show',
                   '--name-status',
                   '--diff-filter=AM',
                   '--pretty=format:',
                   commit.sha1],
                  stdout=PIPE, stderr=PIPE, check=False, encoding='utf-8')

        if cmd.returncode:
            logger.error('git show failed with code %d: %s',
                         cmd.returncode, cmd.stderr)
            sys.exit(1)

        if not cmd.stdout:
            logger.warning('No files changed. Skipping')
            continue

        # Parse the list of files and filter AI files of interest.
        commit.parse_file_list(cmd.stdout)
        logger.info('File list parsed')

        ai_files = [path for path in commit.files if path.suffix == '.ai']

        if not ai_files:
            logger.info('No AI files changed. Skipping')
            continue

        # Generate/update changelog for each modified AI file.
        for ai_path in ai_files:
            logger.info('Generating changelog for %s version %s',
                        ai_path, commit.version)

            changelog_path = ai_path.with_suffix('.changelog.md')

            # Cache the correponding changelog if it exists already.
            if changelog_path not in changelogs and changelog_path.is_file():
                changelogs[changelog_path] = changelog_path.read_text(encoding='utf-8')

            file_blob_url = make_github_blob_url(github_repository, commit, ai_path)
            entry_heading = f'## [{commit.version}]({file_blob_url})'

            changelogs[changelog_path] = \
                f'{entry_heading}\n\n{commit.clean_body}\n' + \
                changelogs[changelog_path]

    logger.info('All changes processed')

    num_changelogs = len(changelogs)
    for i, (path, contents) in enumerate(changelogs.items()):
        path.write_text(contents, encoding='utf-8')
        logger.info('[%2d/%2d] Saved changelog %s', i + 1, num_changelogs, path)

    logger.info('All changelogs saved')
