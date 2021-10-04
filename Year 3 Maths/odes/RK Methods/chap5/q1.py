# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 11:14:35 2021

@author: Jake
"""

from sympy import *

# Define RK method
A = Matrix([[0, 0, 0, 0, 0],
            [Rational(1,4), 0, 0, 0, 0 ],
            [Rational(1,2), 0, 0, 0, 0 ],
            [0, Rational(1,2), Rational(1,4), 0, 0],
            [0, Rational(1,6), -Rational(1,3), Rational(1,6), 0]])
b = Matrix([[-1], [Rational(2,3)], [-Rational(1,3)], [Rational(2,3)], [1]])
e = ones(5, 1)

# Calculate coefficients of R(z)
for k in range(4):
    display(b.T * A ** k * e)  