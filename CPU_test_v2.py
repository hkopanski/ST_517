#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 01:53:27 2020

@author: hkuser
"""

import numpy as np
from timeit import default_timer as timer

def pow(a, b):
    return a ** b

def main():
    vec_size = 1000000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    c = pow(a, b)
    duration = timer() - start

    print(duration)

if __name__ == '__main__':
    main()