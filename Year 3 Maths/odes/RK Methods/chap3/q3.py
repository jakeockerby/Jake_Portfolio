# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:13:10 2021

@author: Jake
"""

import numpy as np
import pandas as pd
from sympy import *

# Declare symbolic variables
a21, b1, b2, c2 = symbols('a21, b1, b2, c2')
b1 = Rational(1,3)

# Define order conditions
eqn1 = b1 + b2 - 1
eqn2 = b2 * c2 - Rational(1,2)
eqn3 = a21 * b2 - Rational(1,2)

# Solver order conditions
print(solve((eqn1, eqn2, eqn3), (a21, b2, c2)))