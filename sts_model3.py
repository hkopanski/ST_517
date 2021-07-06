#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:08:45 2020

@author: hkuser
"""
from statsmodels.stats.power import TTestIndPower
import statistics as sts

quiz6data = [8,6.5,4.25,6.25,4,9,6.5,3.75,7,7.75,7,6,2.25,8.25,
             4.5,5.75,5.75,2.5,6.5,8.75,7,1.75,3.5,9,5.5,8.5,
             7.5,8.25,5.25,4.5,3.5,8.25,4.75,5.75,6.25,3,6,2,
             2.25,6.25,3.5,7.5,4.5,6.75,6]

data_mean = sts.mean(quiz6data)
data_sdev = sts.mean(quiz6data)

effect = data_mean/data_sdev
alpha = 0.01
power = 0.8

tt_solve_power(effect_size=effect, 
                                        nobs=None, 
                                        alpha=alpha, 
                                        power=power, 
                                        alternative='one-sided')

