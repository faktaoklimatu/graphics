This repository contains all graphics, including both the source and published files, created for our websites covering climate change. The websites can be found at faktaoklimatu.cz (in Czech, currently the biggest site), faktyoklime.sk (in Slovak) and factsonclimate.org (in English, currently only a titlepage placeholder).

## Table of Contents

* [Repository Structure](#repository-structure)
* [Committing Guidelines](#committing-guidelines)
* [Fonts We Use](#fonts-we-use)
* [License](#license)
* [See Also](#see-also)

## Repository Structure

The repository is organised into two main directories: a) `data-visualization` which contains the source (AI) and published (PDF) files and changelogs for all our graphics, and b) `Brand` containing source files for the _Fakta o klimatu_ visual brand.

The `data-visualization` directory is furthermore structured hierarchically as follows:

1.  The first level of the hierarchy divides the graphics into (at the moment) five **broad categories**: `climate-indicators`, `emissions`, `energetics`, `future` and `policies`.
2.  At the second level we divide the graphics into four **geographic regions**: `czechia`, `slovakia`, `european-union` or `world`.

    This classification is common among all first-level categories, i.e. we can have `climate-indicators/world/` as well as `policies/world/` or `policies/european-union/`.
3.  The **topic** of a graphic or a set of graphics is specified at the third level.

    This can be, for example, `ghg-emissions-in-czechia-by-sector` for the [donut chart](https://faktaoklimatu.cz/infografiky/emise-cr-detail) of Czechia's greenhouse gas emissions (and its variations) or `carbon-pricing` for the [map](https://faktaoklimatu.cz/infografiky/zpoplatneni-emisi-svet) of carbon pricing schemes in countries across the world.
4.  The **language** and the **slug** of a specific graphic is given in its file name in the format `<language>-<slug>.ai`, e.g. `cs-emise-cr.ai` or `en-emissions-czechia.ai`.

    The language is specified by its two-letter [ISO 639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), for instance `cs` for Czech, `en` for English, `sk` for Slovak, `fa` for Persian, etc.

    The _slug_ is a simplified version of the title. It is mainly used in URLs. From the file name `cs-body-zlomu-3.pdf` we can infer that the language of the graphic is Czech and that it is most likely available at <https://faktaoklimatu.cz/infografiky/body-zlomu-3>. (It indeed is!)

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

Every AI file has a corresponding changelog file associated with it. The changelog file name is the same as the source file except for the extension `.changelog.md`. For instance, the changelog associated with the AI file `cs-emise-cr.ai` is called `cs-emise-cr.changelog.md`.

Every time a change is made to an AI file, an entry is added to the corresponding changelog. The entry consists only of the body of commit message, i.e. the third and following lines. The graphic version is automatically derived from the date of the commit, i.e. a change committed on March 15, 2020 would automatically be assigned the version `2020-03-15`. (Though this can be overridden, see below.)

We follow several established conventions for writing commit messages in the repository (see below for examples):

* Keep the first line (subject) of the commit message to 50 characters or fewer. Keep the second line empty. Wrap all subsequent lines (the body) at 72 characters.
* Start the subject line with a capital letter. Do not end it with a period.
* Use the imperative mood to describe the changes.
* List each change as an individual item in a bulleted list. Use the hyphen (`-`) as the bullet point.
* Start the list item with a capital letter and end it with a period.
* Write `[skip]` or `[ignore]` on a separate line to avoid creating a changelog entry.
* Write `[version=yyyy-mm-dd]` on a separate line to enforce a version different from the one that would be automatically derived from the commit date.

If several AI files are changed in a single commit, the generated changelog entry and version identifier will be the same for all of them.

If multiple commits are pushed at once, all the changes are processed and the changelogs are updated in one subsequent commit.

**Notice:** Since the state of the repository may change after pushing changes (either by other contributors or by the automated generation of changelogs), it is advisable to pull from the repository before pushing any new changes. The preferred practice is to run `git pull --rebase` before each editing session. In case you already have uncommitted changes, use `git pull --rebase --autostash`.

**Example:** The following commit message

    Fix typos and color in CO2 concentrations graphic

    - Change 'CO2' to 'O2' in 'Decrease in the concentration of O2'.
    - Fix spelling in legend.
    - Change red color to match FoK color palette.
    - Darken the whites and lighten the blacks.

would generate a changelog entry such as (assuming it was committed on February 19, 2021)

>   [**2021-02-19**](#)
>
>   - Change 'CO2' to 'O2' in 'Decrease in the concentration of O2'.
>   - Fix spelling in legend.
>   - Change red color to match FoK color palette.
>   - Darken the whites and lighten the blacks.

with the version link pointing to to the corresponding revision of the source AI file.

Notice that the subject line (“Fix typos and color in CO2 concentrations graphic”) is discarded and only the commit message body is used for the changelog.

**Example:** The following commit message **forces a specific version** to be displayed in the changelog

    Data update

    - Update for emissions data from 2020.

    [version=2021-01-30]

It would generate the following entry, independent of the commit date:

>   [**2021-01-30**](#)
>
>   - Update for emissions data from 2020.

**Example:** The following message would enforce that the **commit be skipped** for the purposes of changelog generation and no entry would be added:

    Typo update

    - Fix wrong year in the title (2019 → 2020).

    [skip]

## Fonts We Use

- Titles: [Akrobat](https://www.fontfabric.com/fonts/akrobat/)
- Everything else: [Roboto](https://fonts.google.com/specimen/Roboto)

<!--- ## Templates

TBD

## Typography Guidelines

TBD --->

## License

All our graphics are licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

## See Also

* [web-cz](https://github.com/faktaoklimatu/web-cz), [web-sk](https://github.com/faktaoklimatu/web-sk) and [web-en](https://github.com/faktaoklimatu/web-en) – repositories with sources for the Czech, Slovak and English language versions of our website, respectively
* [web-core](https://github.com/faktaoklimatu/web-core) – repository with source code shared among all the language variants
