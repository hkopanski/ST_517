#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 02:06:38 2020

@author: hkuser
"""

import numpy as np
import pandas as pd
from scipy.stats import chi2

a1 = [10,29,9]
a2 = [38,30,34]

b1 = []
b2 = []


c1 = []
c2 = []


alpha = 0.05

stripped_array = np.array([a1,a2])
df_array = pd.DataFrame([a1,a2])
row_ = stripped_array.shape[0]
col_ = stripped_array.shape[1]

df = (row_-1)*(col_-1) 

for i in range(len(a1)):
    eij = (stripped_array[0].sum()*stripped_array[:,i].sum())/stripped_array.sum()
    b1.append((stripped_array[0,i]-eij)**2/eij)
    c1.append(eij)

for i in range(len(a2)):
    eij = (stripped_array[1].sum()*stripped_array[:,i].sum())/stripped_array.sum()
    b2.append((stripped_array[1,i]-eij)**2/eij)
    c2.append(eij)
    
df_table1 = pd.DataFrame([c1,c2])
df_table2 = pd.DataFrame([b1,b2])
chi_stat = sum(b1)+sum(b2)
p_value = 1 - chi2.cdf(chi_stat,df)

print("="*75)
print(f"The p value is:          {round(p_value,4)}")
print(f"The Chi Square value is: {round(chi_stat,3)}")
print("="*75)

if p_value > alpha:
    print("We cannot reject the null hypothesis.")
else:
    print("We reject the null hypothesis.")

print("="*75)
print(df_table1)
print("="*75)
print(df_table2)
print("="*75)