#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 22:37:08 2020

@author: hkuser
"""

import numpy as np
import pandas as pd
from scipy.stats import chi2

a1 = [13243,13044,15018]
a2 = [2457,1771,1950]
a3 = [10786,11273,13068]
a4 = [240,214,201]
a5 = [931,894,972]
a6 = [14,11,11]
a7 = [196,144,152]

b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []

c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []

alpha = 0.05

stripped_array = np.array([a1,a2,a3,a4,a5,a6,a7])
df_array = pd.DataFrame([a1,a2,a3,a4,a5,a6,a7])
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
    
for i in range(len(a3)):
    eij = (stripped_array[2].sum()*stripped_array[:,i].sum())/stripped_array.sum()
    b3.append((stripped_array[2,i]-eij)**2/eij)
    c3.append(eij)

for i in range(len(a1)):
    eij = (stripped_array[0].sum()*stripped_array[:,i].sum())/stripped_array.sum()
    b4.append((stripped_array[0,i]-eij)**2/eij)
    c4.append(eij)

for i in range(len(a2)):
    eij = (stripped_array[1].sum()*stripped_array[:,i].sum())/stripped_array.sum()
    b5.append((stripped_array[1,i]-eij)**2/eij)
    c5.append(eij)
    
for i in range(len(a3)):
    eij = (stripped_array[2].sum()*stripped_array[:,i].sum())/stripped_array.sum()
    b6.append((stripped_array[2,i]-eij)**2/eij)
    c6.append(eij)
    
for i in range(len(a3)):
    eij = (stripped_array[2].sum()*stripped_array[:,i].sum())/stripped_array.sum()
    b7.append((stripped_array[2,i]-eij)**2/eij)
    c7.append(eij)

df_table = pd.DataFrame([c1,c2,c3,c4,c5,c6,c7])    
chi_stat = sum(b1)+sum(b2)+sum(b3)+sum(b4)+sum(b5)+sum(b6)+sum(b7)
p_value = 1 - chi2.cdf(chi_stat,df)

print("="*50)
print(f"The p value is:          {round(p_value,4)}")
print(f"The Chi Square value is: {round(chi_stat,2)}")
print("="*50)

if p_value > alpha:
    print("We cannot reject the null hypothesis.")
else:
    print("We reject the null hypothesis.")

print("="*50)
print(df_table)
print("="*50)
