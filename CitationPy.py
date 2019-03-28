# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 1.0.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

#Add Dependencies
# %matplotlib inline
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
#import folium

# ## Importing CSV Data
#
#

#Import citation data from csv
citation_raw = pd.read_csv("Parking_Citations.csv")
citation_df = citation_raw


# +
#Name of columns 
#citation_df.columns.tolist()
# -

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

#Take all rows where column values are not equal to zero
citation_df3 = citation_df2[(citation_df2[["Ticket number", "Issue Date","Issue time","Make","Color","Latitude","Longitude",]] != 0)]
citation_df3.head()


#Drop all rows with blank cells
citation_df4 = citation_df3.fillna("")


# +
#citation_df4.count()
# -

citation_df4["Make"].replace("", np.nan, inplace=True)
citation_df4.dropna(subset = ["Make"], inplace = True)

# +
#Sort values by make of car
#citation_df4.sort_values(["Make"],ascending=True)
# -


Sample_data = citation_df4.sample(frac=0.10, random_state = 1 )

Sample_data.head()

#Replace duplicates for all makes in top 30
citation_df4["Make"] = citation_df4["Make"].replace({'TOYT': 'TOYOTA', 'TOYO': 'TOYOTA'})
citation_df5 = citation_df4["Make"].value_counts()
citation_df6 = citation_df5.rename_axis('Make').reset_index(name='counts')
citation_df7 = citation_df6.head(25)


citation_df7.head()

#Bar plot for top 25 make of vehicles that got citations
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
x_axis=np.arange(len(citation_df7["Make"]))
plt.bar(x_axis,citation_df7["counts"], color="blue" )
plt.xlabel('Make', fontsize=18)
plt.ylabel('Counts', fontsize=18)
plt.xticks(x_axis, citation_df7["Make"], fontsize=12, rotation=90,)
plt.title('Top 25 Citations by Make of Cars', fontsize=25)
fig.savefig("make_chart.png")
plt.show()
plt.clf()

#Replace duplicates for all makes in top 30
citation_df8 = citation_df4["Color"].value_counts()
citation_df9 = citation_df8.rename_axis('Color').reset_index(name='Counts')
citation_df10 = citation_df9.head(10)


#Bar plot for top 25 Color of vehicles that got citations
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
x_axis=np.arange(len(citation_df10["Color"]))
plt.bar(x_axis,citation_df10["Counts"], color=('wheat','black',"grey","silver","blue","red","green","brown","maroon","gold","red","tan"))
plt.xlabel('Color', fontsize=18)
plt.ylabel('Counts', fontsize=18)
plt.xticks(x_axis, citation_df10["Color"], fontsize=18, rotation=30)
plt.title('Top 10 Citations by Color of Cars', fontsize=20)
#plt.figure(figsize=(18,16))
fig.savefig("color_chart.png")
plt.show()
plt.clf()

plt.clf()

# Sampling the models of four cars 
df1 = Sample_data[Sample_data.Make.isin(["BMW","FORD","VOLK","DODG"])]
df1.head()

# Group by make of the cars
df2 = df1.groupby("Make").Make.count()

Sample_data_large = citation_df4.sample(frac=0.50, random_state = 1 )

df3 = Sample_data_large[Sample_data_large.Make.isin(["BMW","FORD","VOLK","DODG"])]
df3.info()

df3 = df3.groupby("Make").Make.count()
df3

Observed = df2
Observed

Observed = pd.DataFrame(Observed)
Observed

Observed.columns.values[0]="Observed"
Observed

overall_ratio = (df3/len(df3)).round(0)
overall_ratio

Expected = overall_ratio * len(Observed)
Expected

Expected= pd.DataFrame(Expected)

Expected.columns.values[0] = "Expected"
Expected

Combined =  pd.concat([Observed, Expected], axis = 1)
Combined

#With fur raws, the degree of freedom is 3
# with a p-value of 0.05, the CL is 1-0.05 = 0.95
Critcal_value = stats.chi2.ppf(q=0.95, df = 3)
Critcal_value

stats.chisquare(Combined["Observed"], Combined["Expected"])


