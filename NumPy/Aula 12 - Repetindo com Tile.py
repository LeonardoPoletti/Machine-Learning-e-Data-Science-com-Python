# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 22:32:50 2017

@author: Leonardo
"""

import numpy as np

a = np.array([1,2,3])

print(np.tile(a, 2),'\n')
print(np.tile(a,3),'\n')

b = np.array([[1,2],[3,4]])

print(np.tile(b,2),'\n')