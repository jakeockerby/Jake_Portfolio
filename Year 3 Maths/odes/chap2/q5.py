# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:05:22 2021

@author: 17006438
"""

import numpy as np
import matplotlib.pyplot as plt
from time import sleep

def rk2(f, ts, y0, h):
    ns = int((ts[1]-ts[0])/h)
    t = np.zeros((ns + 1, 1))
    y = np.zeros((ns + 1, len(y0)))
    y[0, :] = y0
    
    for n in range(ns):
        k1 = f(t[n], y[n])
        k2 =  f(t[n] + h, y[n] + h * k1)
        print(k2)
        sleep(5)
        y[n+1] = y[n] + 0.5 * h * (k1 + k2)
        t[n+1] = t[n] + h
        
    return t, y


def f(t, y):
    return np.array([y[1], - 9.81 / 1 * np.sin(y[0])])

t, y = rk2(f, [0, 5], [np.pi/2,0] , 0.1)
print(t)
print(y)


fig = plt.figure()
plt.plot(t, y[:,0], 'bo-')
plt.xlabel('t')
plt.ylabel('theta')