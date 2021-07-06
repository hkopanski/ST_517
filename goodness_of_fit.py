# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:42:57 2020

@author: halid
"""

import numpy as np
from scipy import stats
from scipy.stats import chi2

a1 = [15,27,31,19,11]
a2 = []

alpha  = 0.01
df = len(a1) - 1 

for i in range(len(a1)):
    a2.append(((a1[i]-np.mean(a1))**2)/np.mean(a1))
    
p_value = 1-chi2.cdf(sum(a2),df)

print("="*50)
print(f"The p value is:          {round(p_value,4)}")
print(f"The Chi Square value is: {round(sum(a2),4)}")
print("="*50)

if p_value > alpha:
    print("We cannot reject the null hypothesis.")
else:
    print("We reject the null hypothesis.")

print("="*50)