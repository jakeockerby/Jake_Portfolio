# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:32:10 2021

@author: Jake
"""

from sympy import *

# Declare symbolic variables
t, a11, a12, a21, a22, b1, b2, c1, c2 = symbols('t, a11, a12, a21, a22, b1, b2, c1, c2')

# Calculate c values
P2 = 1 + binomial(2,1) * binomial(3,1) * (t - 1) ** 1 + binomial(2,2) * binomial(4,2) * (t - 1) ** 2
P1 = 1 + binomial(1,1) * binomial(2,1) * (t - 1) ** 1
c1, c2 = solve(P2 - P1)
print(c1, c2)

# Define order conditions
eqn1 = b1 + b2 - 1
eqn2 = b1 * c1 + b2 * c2 - Rational(1,2)
eqn3 = a11 + a12 - c1
eqn4 = a21 + a22 - c2
eqn5 = a11 * c1 + a12 * c2 - Rational(1,2) * c1 ** 2
eqn6 = a21 * c1 + a22 * c2 - Rational(1,2) * c2 ** 2

# Solve order conditions
print(solve((eqn1, eqn2, eqn3, eqn4, eqn5, eqn6), (a11, a12, a21, a22, b1, b2)))