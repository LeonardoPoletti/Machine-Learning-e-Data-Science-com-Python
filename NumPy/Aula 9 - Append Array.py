# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 22:09:56 2017

@author: Leonardo
"""

import numpy as np

a = np.array([1,2,3])

print(np.append(a,[4,5,6]),'\n')

a = np.array([[1,2], [3,4]])
print (np.append(a, [5,6]),'\n')

print(np.append(a,[[5,6]], axis = 0),'\n')