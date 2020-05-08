# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 22:28:59 2017

@author: Leonardo
"""

import numpy as np

a = np.array([[1,2],[3,4]])

print(np.repeat(a,2), '\n')

print(np.repeat(a,3), '\n')

print(np.repeat(a,2,axis=0),'\n')
print(np.repeat(a,2,axis=1),'\n')

print(np.repeat(3,4),'\n')

