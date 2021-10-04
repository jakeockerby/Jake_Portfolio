# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:51:39 2021

@author: Jake
"""

from sympy import *

# Declare symbolic variables
a21, b1, b2, c1, c2 = symbols('a21, b1, b2, c1, c2')
c1 = Rational(1,4)

# Define order conditions
eqn1 = b1 + b2 - 1
eqn2 = b1 * c1 + b2 * c2 - Rational(1,2)
eqn3 = a21 + c1 - c2
eqn4 = b1 * c1 + b2 * a21 - b1 + b1 * c1

# Solve order conditions
print(solve((eqn1, eqn2, eqn3, eqn4), (a21, b1, b2, c2)))