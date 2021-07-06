#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:14:48 2020

@author: hkuser
"""
import numpy as np
import pandas as pd
from scipy.stats import chi2

variable_p = [0.25, 0.25, 0.5]
variable_actual = [42,44,77]
alpha = 0.05

count_ = sum(variable_actual)

variable_c = []
variable_label = []
var_actual_pro = []

for i in range(len(variable_p)):
    variable_label.append('var'+str(i))
    var_actual_pro.append(variable_actual[i]/count_)
    variable_c.append(variable_p[i]*count_)

df_data = { 'Actual': pd.Series(variable_actual, index = variable_label),
        'Proportion': pd.Series(variable_p, index = variable_label), 
        'Actual Pro': pd.Series(var_actual_pro, index = variable_label)}

df_variable = pd.DataFrame(df_data)
df_variable['Expected'] = df_variable['Proportion']*count_
df_variable['Actual - Expected'] = (df_variable['Actual'] - df_variable['Expected'])**2
df_variable['(A-E)**2 / n'] = df_variable['Actual - Expected']/df_variable['Expected']

chi_stat = df_variable['(A-E)**2 / n'].sum()
df = len(variable_actual)-1
p_value = 1 - chi2.cdf(chi_stat,df)

print('='*100)
print(f'The chi stat is: {round(chi_stat,4)}')
print(f'The p value is: {round(p_value,4)}')
print(f'The df is: {round(df,4)}')
print('='*100)
if p_value > alpha:
    print("We cannot reject the null hypothesis.")
else:
    print("We reject the null hypothesis.")
print('='*100)
print(df_variable)
print('='*100)