#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:54:17 2020

@author: hkuser
"""


# estimate sample size via power analysis
from statsmodels.stats.power import TTestIndPower
# parameters for power analysis
effect = 0.8
alpha = 0.01
power = 0.8

quiz6data = [8,6.5,4.25,6.25,4,9,6.5,3.75,7,7.75,7,6,2.25,8.25,4.5,5.75,5.75,2.5,6.5,8.75,7,1.75,3.5,9,5.5,8.5,7.5,8.25,5.25,4.5,3.5,8.25,4.75,5.75,6.25,3,6,2,2.25,6.25,3.5,7.5,4.5,6.75,6]
# perform power analysis
analysis = TTestIndPower()
result = analysis.solve_power(effect, power=power, nobs1=None, ratio=1.0, alpha=alpha)
print('Sample Size: %.3f' % result)