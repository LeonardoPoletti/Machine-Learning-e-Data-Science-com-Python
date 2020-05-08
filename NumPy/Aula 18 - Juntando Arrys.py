# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:47:10 2017

@author: Leonardo
"""

import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
d = np.array([[7,8],[9,10]])

c = np.concatenate((a,b), axis=0)
print(c,'\n')

e = b.T #Matriz Transposta
c = np.concatenate((a,e), axis=1)
print(c,'\n')

c = np.concatenate((a,d), axis=1)
print(c,'\n')

