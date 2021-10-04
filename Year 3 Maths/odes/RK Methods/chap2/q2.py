# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:15:45 2021

@author: Jake
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table


# ODE function
def f(t, y):
    return t + y


# Exact solution
def exact(t):
    return 3 * np.exp(t) - t - 1

# IVP parameters
tspan = [0, 2]
h = 0.4
y0 = [2]

# Calculate exact solution for plotting
texact = np.linspace(tspan[0], tspan[1], 100)
yexact = exact(texact)


# RK2 method
def rk2(f, tspan, y0, h):
    
    nsteps = int((tspan[1] - tspan[0]) / h)
    t = np.zeros((nsteps + 1, 1))
    y = np.zeros((nsteps + 1, len(y0)))
    y[0,:] = y0
    
    for n in range(nsteps):
        k1 = f(t[n], y[n,:])
        k2 = f(t[n] + h, y[n,:] + h * k1)
        y[n+1,:] = y[n,:] + 0.5 * h * (k1 + k2)
        t[n+1] = t[n] + h
    
    return t, y


# Solve IVP
t, y = rk2(f, tspan, y0, h)

# Output table
table = Table([t[:,0], y[:,0]], names=('t', 'RK2'))
table['t'].format = '{:1.1f}'
table['RK2'].format = '{:1.4f}'
print(table)

# Plot solution
fig = plt.figure()
plt.plot(texact, yexact, 'k-', label = 'Exact')
plt.plot(t, y, 'bo-', label = 'RK2')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.show()

fig.savefig('../ODEs_notes/Images/solution_2.png')