# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:14:53 2021

@author: Jake
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table


# Euler method
def euler(f, tspan, y0, h):
    
    nsteps = int((tspan[1] - tspan[0]) / h)
    t = np.zeros((nsteps + 1, 1))
    y = np.zeros((nsteps + 1, len(y0)))
    y[0,:] = y0
    
    for n in range(nsteps):
        y[n+1,:] = y[n,:] + h * f(t[n], y[n,:])
        t[n+1] = t[n] + h
    
    return t, y


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

# Solve IVP
t, y = euler(f, tspan, y0, h)

# Output table
table = Table([t[:,0], y[:,0]], names=('t', 'Euler'))
table['t'].format = '{:1.1f}'
table['Euler'].format = '{:1.4f}'
print(table)

# Calculate exact solution for plotting
texact = np.linspace(tspan[0], tspan[1], 100)
yexact = exact(texact)

# Plot solution
fig = plt.figure()
plt.plot(texact, yexact, 'k-', label = 'Exact')
plt.plot(t, y, 'bo-', label = 'Euler')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.show()

fig.savefig('../ODEs_notes/Images/solution_1.png')