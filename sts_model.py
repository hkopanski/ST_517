#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:14:34 2020

@author: hkuser
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from scipy.stats import t

s_norm = np.random.normal(size=1000)
t_norm = np.random.standard_t(5,1000)

range_vals = np.linspace(-4,4,1000)
norm_vals = []

for i in range(1000):
    norm_vals.append(norm.cdf(range_vals[i]))
    
#sns.distplot(s_norm,hist = False, bins = 100)
#sns.distplot(t_norm,hist = False, bins = 100)

sns.distplot(norm_vals,hist = True, bins = 100)