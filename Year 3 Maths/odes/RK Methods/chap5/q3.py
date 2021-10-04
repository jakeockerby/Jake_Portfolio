# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:03:39 2021

@author: Jake
"""

from sympy import *
import numpy as np
import matplotlib.pyplot as plt
init_printing()

z, y = symbols('z, y')

# Define RK method
A = Matrix([[Rational(1,3), 0],
            [1, 0]])
ebT = Matrix([[Rational(3,4), 0], [0, Rational(1,4)]])
I = eye(2)

# Calculate R(z)
def P(z):
    return (I - z * A + z * ebT).det()
def Q(z):
    return (I - z * A).det()
R = P(z) / Q(z)
print('R(z) = ', simplify(R))


# Generate z values
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = X + Y * 1j

# Define stability function
R = (48 + 32 * Z + 5 * Z ** 2) / (48 - 16 * Z)

# Plot stability region
fig = plt.figure()
plt.contourf(X, Y, abs(R), levels=[0, 1], colors='#99ccff')
plt.contour(X, Y, abs(R), colors= 'k', levels=[0, 1])
plt.axhline(0, color='k', linewidth=1)
plt.axvline(0, color='k', linewidth=1)

plt.axis('equal')
plt.axis([-12, 2, -6, 6])
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()

# fig.savefig('../ODEs_notes/Images/solution_6.png')