# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:48:30 2017

@author: Leonardo
"""

import numpy as np

a = np.array([10,20, 30, 40])
print(a)
print(type(a))
print('################################################')

mat = np.array([[1,2],[3,4]])
print('|%s %s|\n|%s %s|\n' % (mat[0,0], mat[0,1], mat[1,0], mat[1,1]))

print(mat[-1,-1])
print(mat[1,:])
print(mat[:,0])
print()
print(mat.transpose())
print()

m1 = np.array([[1, 2], [3,4]])
m2 = np.array([[5,6], [7,8]])
print(m1+m2)
print()
print(m1-m2)
print()
print(m1*m2)
print()

m3 = np.array([1,2,3,4])
print(m3.sum())
print(m3.argmax())
print(m3.argmin())