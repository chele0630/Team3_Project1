# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
<<<<<<< HEAD
#       jupytext_version: 1.0.5
=======
#       jupytext_version: 1.0.4
>>>>>>> 5641e3ddf060da48377e3380dabe54e84a915765
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

<<<<<<< HEAD
# +
#Add Dependencies

=======
#Add Dependencies
# %autosave 0
>>>>>>> 5641e3ddf060da48377e3380dabe54e84a915765
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
#import folium
<<<<<<< HEAD
# -
=======
>>>>>>> 5641e3ddf060da48377e3380dabe54e84a915765

# ## Importing CSV Data
#
#

#Import citation data from csv
citation_raw = pd.read_csv("Parking_Citations.csv")
citation_df = citation_raw
citation_df.head()

#Name of columns 
citation_df.columns.tolist()

# ## Cleaning Columns from Dataset

# +
#Drop columns that are not needed
citation_df1 = citation_df.drop(["Meter Id","Marked Time","RP State Plate","Plate Expiry Date","VIN","Location","Route","Agency","Violation code","Body Style", "Violation Description", "Fine amount"], axis = 1)
citation_df1.head()

#Drop Lat and Lon = 99999
citation_df2 = citation_df1[(citation_df1["Latitude"] !=99999.000) & (citation_df1["Longitude"] !=99999.000)]
citation_df2.head()

# -

citation_df2.count()

<<<<<<< HEAD
#Take all rows where column values are not equal to zero
citation_df3 = citation_df2[(citation_df2[["Ticket number", "Issue Date","Issue time","Make","Color","Latitude","Longitude",]] != 0)]
citation_df3.head()


#Drop all rows with blank cells
citation_df4 = citation_df3.fillna("")


citation_df4.count()

citation_df4["Make"].replace("", np.nan, inplace=True)
citation_df4.dropna(subset = ["Make"], inplace = True)

citation_df4.sort_values(["Make"],ascending=True)


citation_df4.info()

citation_df4["Make"].unique()

# +
#Check the total counts in each category
citation_df4["Make"].value_counts()
=======
# +
#Take all rows where column values are not equal to zero
citation_df3 = citation_df2[(citation_df2[["Ticket number", "Issue Date","Issue time","Make","Color","Latitude","Longitude",]] != 0)]

#Drop all rows with blank cells
citation_df4 = citation_df3.fillna("")
citation_df4.count()

# +
#Check the total counts in each category
citation_df3["Make"].value_counts()
>>>>>>> 5641e3ddf060da48377e3380dabe54e84a915765
#citation_df3["Color"].value_counts()


# -


