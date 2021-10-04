# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:28:16 2021

@author: Jake
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table


# ERK method
def erk(f, tspan, y0, h):
    
    nsteps = int((tspan[1] - tspan[0]) / h)
    t = np.zeros((nsteps + 1, 1))
    y = np.zeros((nsteps + 1, len(y0)))
    y[0,:] = y0
    
    for n in range(nsteps):
        k1 = f(t[n], y[n])
        k2 = f(t[n] + 1 / 5 * h, y[n] + 1 / 5 * h * k1)
        k3 = f(t[n] + 3 / 4 * h, y[n] + h * (-31 / 32 * k1 + 55 / 32 * k2))
        k4 = f(t[n] + h, y[n] + h * (9 * k1 - 120 / 11 * k2 + 32 / 11 * k3))
        y[n+1] = y[n] + h * (125 / 264 * k2 + 16 / 33 * k3 + 1 / 24 * k4)
        t[n+1] = t[n] + h
    
    return t, y


# ODE function
def f(t, y):
    return t - y


# Exact solution
def exact(t):
    return t + 2 * np.exp(-t) - 1


# IVP parameters
tspan = [0, 2]
h = 0.4
y0 = [1]

# Solve IVP
t, y = erk(f, tspan, y0, h)

# Output table
table = Table([t[:,0], y[:,0], exact(t[:,0]), abs(exact(t[:,0]) - y[:,0])], names=('t', 'ERK', 'Exact', 'Error'))
table['t'].format = '{:1.1f}'
table['ERK'].format = '{:1.4f}'
table['Exact'].format = '{:1.4f}'
table['Error'].format = '{:1.2e}'
print(table)

# Calculate exact solution for plotting
texact = np.linspace(tspan[0], tspan[1], 100)
yexact = exact(texact)

# Plot solution
fig = plt.figure()
plt.plot(texact, yexact, 'k-', label = 'Exact')
plt.plot(t, y, 'bo-', label = 'ERK')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.show()

fig.savefig('../ODEs_notes/Images/solution_4.png')