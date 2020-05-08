# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:55:59 2017

@author: Leonardo
"""
import numpy as np

m1 = np.array([[1,2,3],[4,5,6]])
m2 = np.array([[7,8,9],[10,11,12]])
print(m1 , '\n')
print(m2 , '\n')

print(m2 / m1 , '\n')

print(np.matrix.round(m2/m1), '\n')

print(m2 * 10 ,'\n')

print(m1 + 5 , '\n')

print(m1 * m2 , '\n')

print(m1 **2, '\n')
