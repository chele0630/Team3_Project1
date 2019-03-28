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
 
### Hypothesis Validation
* Purpose One
   * Null hypothesis: there is no significant relationship between the make of cars and the number of citations. 
   * Alternate hypothesis: there is a significant relationship between the make of cars and the number of citations.
* Purpose Two
   * Null Hypotheses: there is no a significant relationship between color of the car and the number of parking citations.
   * Alternate hypothesis: there is a significant relationship between color of the car and the number of parking citations. 
* Since the chi-square value of 25599 at a confidance level of 95% exceeds the CV of 7.8114. We, therefore, conclude that there is a difference between the two groups is stastically significant. Also, the p-vale was zero indicates that the null phyptheses is false. We reject the null hypothesis.

### Key Documents

The following data sets used throughout the project.

* a dataset was downloaded from the City of Los Angeles for the months of May through July 2018 in csv format.
* Folium was used and various plug-ins were used to create interactive heat maps and location markers

### Findings
* Toyota tops the list of the make of vehicles that received the most citation at 74K followed by Honda at 47K and Ford at 35K. Nissan was fourth in the list at 31K and Chevy ranked no.5 at 27K. 
* White colored vehicles received the most citations followed very closely by black and gray colored vehicle. Silver ranked at no.4 and blue ranked no. 5. 

[![INSERT YOUR GRAPHIC HERE](https://github.com/ButtonWalker/Team3_Project1/blob/master/CitaLocationMap.png)]()

[![INSERT YOUR GRAPHIC HERE](https://github.com/ButtonWalker/Team3_Project1/blob/master/CitaHeatMap.png)]()

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
   from datetime import datetime
   import folium
   from folium.plugins import fast_marker_cluster as fmc
   import pyproj
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

[![GIT Workflow](https://github.com/ButtonWalker/Team3_Project1/blob/master/GitWorkFlow.png)]()
```sh
Name Features (featureKW01)
Name Bugs (BugKW01) feature number and bug number to match
```
## Acknowledgments
Giving credit to those who helped
```sh
Hat tip to anyone whose code was used
Inspiration
etc
```
