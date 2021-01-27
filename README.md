I am just a baby readme page. But expect me to grow up soon. :) 


### Commiting guidelines
After each push of an .ai file (commited without `[skip]` or `[ignore]`), a changelog entry is automatically generated (in a separate commit). The changelog contains the title and a description from the commit message and automatically dates the entry to the date of the commit message. 

Conventions for writing commit messages:
* Each change is listed in an individual line
* A list item starts with a capital letter and ends with a periods. `- I am a single change description.`
* Use `[skip]` or `[ignore]` in a commit message (in a seperate line) to avoid changelog entry
* Use `[version=yyyy-mm-dd]` to overwrite the date of the changelog entry



An example of a **regular commit message** generating a changelog entry
```
git commit -m "Fixed typos and color

- CO2 changed to O2 in 'Decrease in the concentration of O2'.
- Fixed red color to match the red from FoK color palette."
```



An example of a **commit message w/ version date fix**
```
git commit -m "Data update

- Data vis updated to emission data from 2020.
[version=2021-01-01]"
```
An example of a **commit message ignored in the changelog**
```
git commit -m "Typo update

- Fixed wrong year in the title (2019 -> 2020).
[skip]"
```

In case of a push of multiple commits, all changelog are processed at once and updated in one subsequent commit. -> So it is necessary, to remember to "pull" after each push. 
Ideally, before each change, use `git pull --rebase`. In case you already have uncommited changes, use `git pull --rebase --autostash`. 

### Fonts we use: 
- Title font: [Akrobat](https://www.fontfabric.com/fonts/akrobat/)
- Everything else: [Roboto](https://fonts.google.com/specimen/Roboto)

### Templates
TBD

### Typo Guidelines
TBD

### Folder structure

├── Data visualization

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Main categories _(climate indicators, energetics, ...)_

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Region _(Czechia, Slovakia, EU, World)_

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Topic of datavis

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── cs-_slug_.ai

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── cs-_slug_.pdf

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── en-_slug_.ai

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── en-_slug_.pdf
