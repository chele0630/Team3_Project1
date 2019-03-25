[![INSERT YOUR GRAPHIC HERE](https://ladot.lacity.org/sites/g/files/wph266/f/styles/banner/public/lacityp_027861_0.jpg?itok=j4htAmA6)]()

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Team 3 Project 1](#team-3-project-1)
* [Purpose of the Analysis](#purpose-of-the-analysis)
* [Key Documents](#key-documents)
* [Coding Style](#coding-style)
* [API Calls](#api-calls)
* [Coding Documentation](#coding-documentation)
* [Authors](#authors)
* [Acknowledgments](#acknowledgments)

# Team 3 Project 1

Team 3 project is done to uncover patterns in parking activity around the Las Angeles area. We will examine realtionships between vehicle makes and parking citations, and vehicle color and parking citations.

### Purpose of the Analysis

We have two main purposes of the analysis:

* The first purpose is to examine if a relationship exists between vehicle make and parking citations.
* The second purpose is to examine if a relationship exists beteen vehicle color andd parking citations.
* The team will examine and plot citation locations to evaluate a possible correlation between parking citations adn the surrounding area
    * Dining
    * Housing
    * Bar
    * Night club

### Key Documents

The following data sets used throughout the project.

* a dataset was downloaded from the City of Los Angeles for the months of May through July 2018 in csv format.
* a dataset was downloaded from the California DMV in csv format.
* and API call from citipy is used.
* an API call to Google places is used.

### Coding Style

Jupyter notebooks will be used. 

List of dependencies:
```sh
   import matplotlib.pyplot as plt
   import pandas as pd
   import numpy as np
   import requests
   import time
   import pprint
   from citipy import citipy
   import gmaps
   import gmaps.datasets
   import scipy.stats as stats
```
### API Calls

[City of Las Angels](https://data.lacity.org/resource/8yfh-4gug.json)

### Coding Documentation
[gmaps](https://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html)

[Citipy](https://github.com/wingchen/citipy)

[Google API](https://developers.google.com/places/web-service/search)

[Folium Mapping](https://python-visualization.github.io/folium/)

## Authors

Ka-Ri Walker - Initial work - [SMU DataTeam 3](https://github.com/ButtonWalker)

Sujita Kapali - Inital Work - [SMU DataTeam 3](https://github.com/SujiKap)

Sisay Teketele - Inital Wark - [SMU DataTeam 3](https://github.com/sisayyt)

## Git Version Workflow

[![GIT Workflow](https://1drv.ms/u/s!Ama2FXUeXhwwgvU3TrYR8LNRYtGBbQ)]()
```sh
Name Features (featureKW01)
Name Bugs (BugKW01) feature number and bug number same
```
## Acknowledgments
Giving credit to those who helped
```sh
Hat tip to anyone whose code was used
Inspiration
etc
```
