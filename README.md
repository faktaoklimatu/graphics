I am just a baby readme page. But expect me to grow up soon. :)

## Repository Structure

The repository is organised into two main directories: a) `data-visualization` which contains the source (AI) and published (PDF) files and changelogs for all our graphics, and b) `Brand` containing source files for the _Fakta o klimatu_ visual brand.

The `data-visualization` directory is furthermore structured hierarchically as follows:

1.  The first level of the hierarchy encompasses a broad categorization into (at the moment) four main categories: `climate-indicators`, `emissions`, `energetics`, `future` and `policies`.
2.  At the second level we divide the graphics into four geographic regions: `czechia`, `slovakia`, `european-union` or `world`.

    This classification is common among all first-level categories, i.e. we can have `climate-indicators/world/` as well as `policies/world/` or `policies/european-union/`.
3.  The topic of a graphic or a set of graphics is specified at the third level.

    This can be, for example, `ghg-emissions-in-czechia-by-sector` for the [donut chart](https://faktaoklimatu.cz/infografiky/emise-cr-detail) of Czechia's greenhouse gas emissions (and its variations) or `carbon-pricing` for the [map](https://faktaoklimatu.cz/infografiky/zpoplatneni-emisi-svet) of carbon pricing schemes in countries across the world.
4.  The language and title of a specific graphic is given in the file name.

    The language is given by its two-letter [ISO 639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

    TODO: Continue.

The `_util` directory contains source code for the repository's automation facilities.

Here is a preview of the directory structure of the repository:

    ├── data-visualization
    │   └── emissions                                   ←  Main category
    │       └── czechia                                 ←  Geographic region
    │           └── ghg-emissions-in-czechia-by-sector  ←  Datavis topic
    │               ├── cs-emise-cr.ai
    │               ├── cs-emise-cr.changelog.md
    │               ├── cs-emise-cr.pdf
    │               ├── en-emissions-czechia.ai
    │               ├── en-emissions-czechia.changelog.md
    │               ├── en-emissions-czechia.pdf
    │               └── ...
    ├── Brand
    │   ├── logo.ai
    │   ├── logo.changelog.md
    │   └── ...
    └── _util
        └── ...

## Committing Guidelines

Each major (published) change in a graphic or set of related graphics should be committed in this repository.

Every AI file has a corresponding changelog file associated with it. The changelog file name is the same as the source file except for the extension `.changelog.md`. For instance,

Every time a change is made to an `.ai` file,
 an entry is added to the corresponding changelog. The changelog contains the title and a description from the commit message and automatically dates the entry to the date of the commit message.

Conventions for writing commit messages:

* First line should not be longer than 50 characters. Subsequent lines should be wrapped at 72 characters.
* Each change is listed on an individual line.
* Each change should be
* A list item starts with a capital letter and ends with a periods. `- I am a single change description.`.
* Use present tense/imperative mood.
* Use `[skip]` or `[ignore]` at the end of a commit message (on a seperate line) to avoid creating a changelog entry.
* Use `[version=yyyy-mm-dd]` to enforce a version different from the one that would be derived from the commit date.

For example, the following commit message

    Fix typos and color in concentrations graphic

    - Change 'CO2' to 'O2' in 'Decrease in the concentration of O2'.
    - Fix red color to match FoK color palette.

would generate a changelog entry such as

>   [**2021-02-19**](#)
>
>   - Change 'CO2' to 'O2' in 'Decrease in the concentration of O2'.
>   - Fix red color to match FoK color palette."

with the version link pointing...

An example of a **commit message w/ version date fix**

```
git commit -m "Data update

- Update to emissions data from 2020.

[version=2021-01-01]"
```

An example of a **commit message ignored in the changelog**

```
git commit -m "Typo update

- Fix wrong year in the title (2019 → 2020).

[skip]"
```

In case multiple commits are pushed at once, all the changes are processed and updated in one subsequent commit. -> So it is necessary, to remember to "pull" after each push.
Ideally, before each session, use `git pull --rebase`. In case you already have uncommitted changes, use `git pull --rebase --autostash`.

## Fonts We Use

- Titles: [Akrobat](https://www.fontfabric.com/fonts/akrobat/)
- Everything else: [Roboto](https://fonts.google.com/specimen/Roboto)

## Templates

TBD

## Typo Guidelines

TBD

## Licensing
