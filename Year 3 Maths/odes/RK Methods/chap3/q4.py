# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:21:46 2021

@author: Jake
"""

from sympy import *

# Declare symbolic variables
a21, a31, a32, a41, a42, a43 = symbols('a21, a31, a32, a41, a42, a43')
b1, b2, b3, b4 = symbols('b1, b2, b3, b4')
c2, c3, c4 = symbols('c2, c3, c4')

# Define unknowns
b1, c2 = 0, Rational(1,5)

# Define order conditions
eqn1 = b1 + b2 + b3 + b4 - 1
eqn2 = b2 * c2 + b3 * c3 + b4 * c4 - Rational(1,2)
eqn3 = b2 * c2 ** 2 + b3 * c3 ** 2 + b4 * c4 ** 2 - Rational(1,3)
eqn4 = b2 * c2 ** 3 + b3 * c3 ** 3 + b4 * c4 ** 4 - Rational(1,4)
eqn5 = b3 * c3 * a32 * c2 + b4 * c4 * (a42 * c2 + a43 * c3) - Rational(1,8)
eqn6 = b3 * a32 + b4 * a42 - b2 * (1 - c2)
eqn7 = b4 * a43 - b3 * (1 - c3)
eqn8 = b4 * (1 - c4)
eqn9 = c2 - a21
eqn10 = c3 - a31 - a32
eqn11 = c4 - a41 - a42 - a43

# Solve order conditions
print(solve((eqn1, eqn2, eqn3, eqn4, eqn5, eqn6, eqn7, eqn8, eqn9, eqn10, eqn11), \
      (a21, a31, a32, a41, a42, a43, b2, b3, b4, c3, c4)))