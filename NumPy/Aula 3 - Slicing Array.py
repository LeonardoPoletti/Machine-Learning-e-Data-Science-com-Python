# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:26:44 2017

@author: Leonardo
"""

l = [20, 30, 10, 40]

print(l)
print(l[1:3])
print(l[::2])

print('########################################')
import numpy as np

a = np.array(l)

print(a)
print(a[1:3])
print(a[::2])

print('########################################')

l2 = l[:]
print(l2)
l2[0] = 1000

print(l)
print(l2)

print('########################################')

b = a[:]
print(b)
b[0] = 1000

print(a)
print(b)


print('########################################')

#b[:] = 42
#print(b)

print('########################################')

c = a.copy()
print(c)
print(a)

c[0] = 0
print(c)
print(a)





















