# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:14:31 2017

@author: Leonardo
"""

import numpy as np

a = np.array([[2,4],[6,8]])
print(a.mean())
print(a.diagonal())
print(a.ndim)

print('##############################################')
      

soma = 0
for i in range(1, 10000001):
    soma +=1
print(soma)
soma2 = np.arange(1, 10000001).sum()
print(soma2)