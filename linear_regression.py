#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:40:31 2020

@author: hkuser
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir(r"/home/hkuser/Documents/SASUniversityEdition/myfolders/SAS_Data")

#Random data
x_vals = np.linspace(1,15,50)
y_vals = np.random.normal(2*x_vals + 5,3)
y_pred = 2*x_vals + 5

df_dict = {"x": pd.Series(x_vals),
           "raw y": pd.Series(y_vals), 
           "pred y": pd.Series(y_pred)}

df = pd.DataFrame(df_dict)

#House data linear regression
df_house = pd.read_table(r"house.txt", delimiter = " ")
df_house['ValRes'] = df_house['Value'] - np.mean(df_house['Value'])
df_house['SqFtRes'] = df_house['SqFt'] - np.mean(df_house['SqFt'])
df_house['VSqFtRes'] = df_house['ValRes']*df_house['SqFtRes']
df_house['ValRes2'] = (df_house['ValRes'])**2
df_house['SqFtRes2'] = (df_house['SqFtRes'])**2   

r_value = df_house['VSqFtRes'].sum()/(df_house['ValRes2'].sum()*df_house['SqFtRes2'].sum())**0.5
r_square = r_value**2

slope = df_house['VSqFtRes'].sum()/df_house['SqFtRes2'].sum()
intercept = np.mean(df_house['Value']) - slope * np.mean(df_house['SqFt'])

#Plotting instructions           
fig, ax = plt.subplots()

ax.scatter(df_house['SqFt'],
        df_house['Value'], 
        label = "Raw Data")

ax.plot(df_house['SqFt'],
        slope * df_house['SqFt'] + intercept, 
        color = "red", 
        label = "Predicted Trend")

plt.legend();