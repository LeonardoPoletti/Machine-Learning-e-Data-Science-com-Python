# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:51:23 2017

@author: Leonardo
"""
import numpy as np

a = np.array([1, 10 + 2j, 20 + 5j], dtype=complex)

print(a,'\n')

print(a[1] + a[2],'\n')
print(a[1] - a[0],'\n')
