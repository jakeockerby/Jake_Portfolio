# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 08:00:56 2021

@author: Jake
"""

import numpy as np
import pandas as pd


# Define a, b and c values
a = [[0,0,0],
     [1/4,1/4,0],
     [0,1,0]]

b = [1/6,2/3,1/6]

c = [0,1/2,1]

# Number of rows
s = len(a)

# Find B(k)
def B(a, b, c):
    L = []
    R = []
    j = 1
    while round(sum(L), 4) == round(sum(R), 4):
        L = []
        R = []
        for i in range(s):
            L.append(b[i]*(c[i]**(j-1)))
        R.append(1/j)
        j += 1
    # print(sum(L))
    # print(sum(R))
    
    K = j-2
    return K


# Find C(k)
def C(a, b, c, K):
    ls = []
    rs = []
    for l in range(1, int(K/2) + 1):
        j = 1
        for i in range(s):
            L = []
            R = []
            for j in range(s):
                L.append(a[i][j]*(c[j]**(l-1)))
                R.append((1/l)*(c[i]**l))
            
            if round(sum(L), 4) == round(sum(R), 4):
                ls.append(round(sum(L), 4))
                rs.append(round(sum(R), 4))
    
    if sum(ls) == sum(rs):
        return 'C({}) is satisfied!'.format(int(K/2))
    else:
        return 0



# Find D(k)
def D(a, b, c, K):
    ls = []
    rs = []
    for l in range(1, int(K/2) + 1):
        i = 1
        for j in range(s):
            L = []
            R = []
            for i in range(s):
                L.append(b[i]*(c[i]**(l-1))*a[i][j])
                R.append((1/l)*(b[j])*(1 - c[j]**l))
            
            if round(sum(L), 4) == round(sum(R), 4):
                ls.append(round(sum(L), 4))
                rs.append(round(sum(R), 4))
    
    if sum(ls) == sum(rs):
        return 'D({}) is satisfied!'.format(int(K/2))
    else:
        return 0



K = B(a, b, c)
print('Maximum Order = ', K)

C = C(a, b, c, K)
if C == 0:
    K -= 1
    C = C(a, b, c, K)
    
print(C)


D = D(a, b, c, K)
if D == 0:
    K -= 1
    D = D(a, b, c, K)

print(D)

print('Method of order ', K)