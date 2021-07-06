#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:34:13 2020

@author: hkuser
"""


import numpy as np
import pandas as pd
from scipy import stats

a1 = [60,300]
a2 = [10,390]

a_array = np.array([a1,a2])

chi2_stat, p_val, dof, ex = stats.chi2_contingency(a_array, correction = False)

df_ex = pd.DataFrame(ex)

print('='*75)
print(f'The Chi statistic: {round(chi2_stat,4)}')
print(f'The p value is: {round(p_val,5)}')
print(f'The degrees of freedom: {dof}')
print('='*75)
print(df_ex)
print('='*75)