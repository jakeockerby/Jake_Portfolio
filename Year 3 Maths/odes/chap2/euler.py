# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:40:59 2021

@author: 17006438
"""

import numpy as np
import matplotlib.pyplot as plt
# from astropy.table import Table

def euler(f, ts, y0, h):
    ns = int((ts[1]-ts[0])/h)
    t = np.zeros(ns + 1)
    y = np.zeros(ns + 1)
    y[0] = y0
    
    for n in range(ns):
        y[n+1] = y[n] + h * f(t[n], y[n])
        t[n+1] = t[n] + h
        
    return t, y

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


def exact(t):
    return 3*np.exp(t) - t - 1




teuler, yeuler = euler(f, [0, 2], 2, 0.4)
t_rk, y_rk = rk2(f, [0, 2], 2, 0.4)

# print(t)
# print(y)

# table = Table([teuler, yeuler, y_rk, exact(teuler), abs(exact(teuler) - yeuler), abs(exact(t_rk) - y_rk)], names=('t', 'Euler', 'RK', 'Exact', 'Error_Euler', 'Error_RK'))
# table['t'].format = '{:1.1f}'
# table['Euler'].format = '{:1.4f}'
# table['RK'].format = '{:1.4f}'
# table['Exact'].format = '{:1.4f}'
# table['Error_Euler'].format = '{:1.4f}'
# table['Error_RK'].format = '{:1.4f}'

# print(table)

# texact = np.linspace(0, 2, 100)
# yexact = exact(texact)

# fig = plt.figure()
# plt.plot(texact, yexact, 'k-', label='Exact')
# plt.plot(teuler, yeuler, 'bo-', label='Euler')
# plt.plot(t_rk, y_rk, 'ro-', label='RK')


# plt.legend()
# plt.xlabel('t')
# plt.ylabel('y')
