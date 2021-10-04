# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:10:14 2021

@author: Jake
"""

import numpy as np

# Define coefficient matrix
A = np.array([[ -80.6, 119.4],
              [ 79.6, -120.4]])

# Calculate stiffness ratio
eigvals = np.linalg.eigvals(A)
S = max(abs(eigvals)) / min(abs(eigvals))
print('S = {:0.2f}'.format(S))
print('max step is h = {:1.4f}'.format(min(-2 / eigvals)))