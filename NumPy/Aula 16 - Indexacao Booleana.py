# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:28:09 2017

@author: Leonardo
"""

import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print(a, '\n')

print(a[a>3], '\n')

idx = (a > 2)
print(idx)