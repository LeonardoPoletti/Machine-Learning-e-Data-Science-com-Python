# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 20:58:18 2017

@author: Leonardo
"""

import pandas as pd

s = pd.Series([1,4,6,5,7,10,6])

print(s)

print(s[2:4])
print(s[5],'\n')

print(s.describe(),'\n')
print(s.mean(),'\n')
print(s.median(),'\n')
print(s.duplicated(),'\n')


s2 = pd.Series([11, 5,8])

s = s.append(s2)

print(s,'\n')