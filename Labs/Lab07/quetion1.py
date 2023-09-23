# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 18:11:38 2021

@author: Ghadir
"""
import numpy as np
import pandas as pd


# You have a series of data that represents the amount of precipitation ech 
#day for a year in a given city.
# Load data file using Pandas
# use Pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv('Seattle2014.csv')['PRCP']
print("\nRainfall values =\n", rainfall[0:30])
Raininches = (rainfall / 254) # 1/10MM -> inches
avgRain = (Raininches.sum()/365)
print("\naverage rain=", np.average(avgRain))

#print("Rain value in inches=\n", Raininches)

#print("Total avg rainfall = ", np.average(rainfall))

# print("Number of values=", Raininches.shape)
# print("Values=", Raininches)

print("\n===================================================================\n")

snowfall = pd.read_csv('Seattle2014.csv')['SNOW']
snowfall[snowfall < 0] = 0 #change negitive number to 0
snowfall[snowfall == 'null'] = 0 # check for null values
print("\nSnowFall values =\n", snowfall[0:30])

Snowinches = snowfall / 254 # 1/10MM -> inches
avgsnow = Snowinches.sum()/365
print("\naverage snow=", avgsnow)

#print("Snow value in inches=\n", Snowinches)

print("\n===================================================================\n")

# Average Snow for January
JanSnowFall = pd.read_csv('Seattle2014.csv')['SNOW'].loc[0:30]
print("\n January Snowfall = \n", JanSnowFall)

janInches = JanSnowFall / 254 # 1/10MM -> inches
janSum = janInches.sum() / 365
print("\nTotal of January Snowfall in Inches = ", janSum)
