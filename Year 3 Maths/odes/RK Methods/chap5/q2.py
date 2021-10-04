# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 11:51:46 2021

@author: Jake
"""

from sympy import *

z, y = symbols('z, y')

# Define RK method
A = Matrix([[Rational(7,24), -Rational(1,24)],
            [Rational(13,24), Rational(5,24)]])
ebT = Matrix([[Rational(1,2), 0], [0, Rational(1,2)]])
I = eye(2)

# Calculate R(z)
def P(z):
    return (I - z * A + z * ebT).det()

def Q(z):
    return (I - z * A).det()

R = P(z) / Q(z)
print('R(z) = ', simplify(R))

# Check roots of Q have positive real parts
roots = solve(Q(z) - 0)
print('roots of Q(z) = ', roots)

# Check E(y) >= 0
E = Q(1j * y) * Q(-1j * y) - P(1j * y) * P(-1j * y)
print('E(y) = ', simplify(E))