# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 10:24:22 2021

@author: Jake
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table


# IRK method
def irk(f, tspan, y0, h):
    
    nsteps = int((tspan[1] - tspan[0]) / h)
    t = np.zeros(nsteps + 1)
    y = np.zeros(nsteps + 1)
    y[0] = y0
    
    for n in range(nsteps):
        
        Y = np.ones((2, 1))
        Ynew = np.ones((2, 1))
        for k in range(100):
            Ynew[0] = y[n] + h * (1/4 * f(t[n] + 1/4 * h, Y[0]))
            if abs(Y[0] - Ynew[0]) < 1e-4:
                break 
            Y[0] = Ynew[0]
        for k in range(100): 
            Ynew[1] = y[n] + h * (1/2 * f(t[n] + 1/4 * h, Y[0]) + 1/4 * f(t[n] + 3/4 * h, Y[1]))
            if abs(Y[1] - Ynew[1]) < 1e-4:
                break 
            Y[1] = Ynew[1]
            
        y[n+1] = y[n] + h * (1/2 * f(t[n] + 1/4 * h, Y[0]) + 1/2 * f(t[n] + 3/4 * h, Y[1]))
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
y0 = 1

# Solve IVP
t, y = irk(f, tspan, y0, h)

# Output table
table = Table([t, y, exact(t), abs(exact(t) - y)], names=('t', 'IRK', 'Exact', 'Error'))
table['t'].format = '{:1.1f}'
table['IRK'].format = '{:1.4f}'
table['Exact'].format = '{:1.4f}'
table['Error'].format = '{:1.2e}'
print(table)

# Calculate exact solution for plotting
texact = np.linspace(tspan[0], tspan[1], 100)
yexact = exact(texact)

# Plot solution
fig = plt.figure()
plt.plot(texact, yexact, 'k-', label = 'Exact')
plt.plot(t, y, 'bo-', label = 'IRK')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.show()

fig.savefig('../ODEs_notes/Images/solution_5.png')