# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:31:05 2021

@author: Jake
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table


# RK4 method
def rk4(f, tspan, y0, h):
    
    nsteps = int((tspan[1] - tspan[0]) / h)
    t = np.zeros((nsteps + 1, 1))
    y = np.zeros((nsteps + 1, len(y0)))
    y[0,:] = y0
    
    for n in range(nsteps):
        k1 = f(t[n], y[n])
        k2 = f(t[n] + 0.5 * h, y[n] + 0.5 * h * k1)
        k3 = f(t[n] + 0.5 * h, y[n] + 0.5 * h * k2)
        k4 = f(t[n] + h, y[n] + h * k3)
        y[n+1,:] = y[n,:] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t[n+1] = t[n] + h
    
    return t, y


# Solve IVP
t, y = rk4(f, tspan, y0, h)

# Output table
table = Table([t[:,0], y[:,0], exact(t[:,0]), abs(exact(t[:,0]) - y[:,0])], names=('t', 'RK4', 'Exact', 'Error'))
table['t'].format = '{:1.1f}'
table['RK4'].format = '{:1.4f}'
table['Exact'].format = '{:1.4f}'
table['Error'].format = '{:1.2e}'
print(table)