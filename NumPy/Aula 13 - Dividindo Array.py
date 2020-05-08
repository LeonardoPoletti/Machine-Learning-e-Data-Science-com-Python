# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 22:36:26 2017

@author: Leonardo
"""

import numpy as np

a = np.array([[1,2,3],[4,5,6]])

print(np.array_split(a, 2, axis =0),'\n')

print(np.array_split(a, 2, axis = 1),'\n')

b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

arrays = np.array_split(b, 2, axis =0)
for array in arrays:
    print (array)
