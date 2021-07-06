#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:14:48 2020

@author: hkuser
"""
import numpy as np
import pandas as pd
from scipy.stats import chi2

horse_p = [0.25,0.5,0.25]
horse_actual = [21,52,23]
count_ = 96

horse_c = []

for i in range(3):
    horse_c.append(horse_p[i]*count_)

df_ = { 'Actual': pd.Series(horse_actual, index = ['Dark','Palomino','Light']), 
        'Proportion': pd.Series(horse_p, index = ['Dark','Palomino','Light'])}

df_horse = pd.DataFrame(df_)
df_horse['Expected'] = df_horse['Proportion']*96
df_horse['Actual - Expected'] = (df_horse['Actual'] - df_horse['Expected'])**2
df_horse['(A-E)**2 / n'] = df_horse['Actual - Expected']/df_horse['Expected']

chi_stat = df_horse['(A-E)**2 / n'].sum()
df = len(horse_actual)-1
p_value = round(chi2.cdf(chi_stat,df),4)

print('='*50)
print(f'The p value is: {p_value}')
print('='*50)