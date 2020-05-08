# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:52:40 2017

@author: Leonardo
"""

import numpy as np

arr = np.array([1,2,3])
print(arr)
arr = np.insert(arr, 1, 10)
print (arr , '\n')

a = np.array([[1,2], [3,4]])
print(a)
print(a.ndim, '\n')

print(a.sum(axis = 0))
print(a.sum(axis = 1), '\n')

a = np.insert(a, 1, 5, axis = 1)
print(a)

print('\n', np.insert(a, 0, 5, axis =0))

