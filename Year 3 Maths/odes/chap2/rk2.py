# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:01:10 2021

@author: 17006438
"""

import numpy as np


def rk2(f, ts, y0, h):
    ns = int((ts[1]-ts[0])/h)
    t = np.zeros(ns + 1)
    y = np.zeros(ns + 1)
    y[0] = y0
    
    for n in range(ns):
        k1 = f(t[n], y[n])
        k2 =  f(t[n] + h, y[n] + h * k1)
        y[n+1] = y[n] + 0.5 * h * (k1 + k2)
        t[n+1] = t[n] + h
        
    return t, y


def f(t, y):
    return t+y

t, y = rk2(f, [0, 2], 2, 0.4)
print(t)
print(y)