# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 22:19:33 2017

@author: Leonardo
"""

import numpy as np

a = np.array([[1,2],[3,4],[5,6]])

print(np.delete(a, 1, axis = 0),'\n')
print(np.delete(a, 0, 1),'\n')

b = np.array([[1,2,3], [4,5,6],[7,8,9],[10,11,12]])
print(b,'\n')
print(np.delete(b, np.s_[::2], axis =0),'\n')