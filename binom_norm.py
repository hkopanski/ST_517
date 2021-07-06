#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:58:25 2020

@author: hkuser
"""


import math
from scipy.stats import binom
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

p = 0.5
n = 10
h = 8
mu = n*p
sigma = (n*p*(1-p))**0.5
calc_list = []
x_vals = list(range(h+1))
x1_vals = list(range(0,h+1,10))
r_val = 5

def combination(x,y):
    z = x - y
    return math.factorial(x)/(math.factorial(y)*math.factorial(z))

def prob(x,y,z):
    return combination(y,z)*x**(z)*(1-x)**(y-z)

for i in range(round(h)+1):
    calc_list.append(prob(p,n,i))

#print(calc_list)
print(f"Calculated Value:    {round(1-sum(calc_list),r_val)}")
print(f"Python Function:     {round(1-binom.cdf(h,n,p),r_val)}")
print(f"Normal Distribution: {round(1-norm.cdf(h,mu,sigma),r_val)}")
print(calc_list)

fig, ax = plt.subplots()
sns.barplot(x = x_vals, y = calc_list)
#ax.set_xticks(x1_vals)
#ax.xaxis.set_major_locator(plt.MaxNLocator(10))
ax.grid()