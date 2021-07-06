#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 11:26:20 2020

@author: hkuser
"""

import numpy as np
import pandas as pd
from scipy.stats import chi2

#Enter the information into this array.
a1 = np.array([
     [10,29,9, 10,15], 
     [38,30,34,25,45],
     [15,5 ,28,18,12]])

#Enter the alpha value
alpha = 0.05

#Calculating the degrees of freedom
row_ = a1.shape[0]
col_ = a1.shape[1]

df = (row_-1)*(col_-1)

#Create tables to store calculated information based on input array.
b1= np.empty((row_, col_))
c1= np.empty((row_, col_))

for i in range(row_):
    for j in range(col_):
        a = np.sum(a1[i])   #Row Total
        b = np.sum(a1[:,j]) #Column Total
        c = np.sum(a1)      #Overall Total
        eij = (a * b) / c
        b1[i][j] = ((a1[i][j]-eij)**2/eij)
        c1[i][j] = (eij)

#Using pandas because it prints nicer
df_table1 = pd.DataFrame(b1)
df_table2 = pd.DataFrame(c1)

#Calculation of statistical values
chi_stat = np.sum(b1)
p_value = 1 - chi2.cdf(chi_stat,df)

#Summary format variables **only for formating the summary**
r_val = 4
sep_len = col_ * len(str(round(df_table2.iloc[0,0],8))) + 3 

#Summary printout and hypothesis decision
print("="*sep_len)
print(f"The p value is:          {round(p_value,r_val)}")
print(f"The Chi Square value is: {round(chi_stat,3)}")
print("="*sep_len)

if p_value > alpha:
    print("We cannot reject the null hypothesis.")
else:
    print("We reject the null hypothesis.")

print("="*sep_len)
print("Contingency Table")
print("="*sep_len)
print(df_table1)
print("="*sep_len)
print("Expected Values")
print("="*sep_len)
print(df_table2)
print("="*sep_len)
