# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:21:00 2017

@author: Leonardo
"""

import pandas as pd
import timeit

titanic = pd.read_csv('titanic.csv')

print(titanic.columns,'\n')

print(titanic['Sex'].describe(),'\n')
print(titanic['Sex'].nbytes,'\n')

inicio = timeit.default_timer()
print(titanic['Sex'] == 'Male','\n')
fim = timeit.default_timer()
print(fim - inicio,'\n')


titanic['Sex'] = titanic['Sex'].astype('category')

print(titanic['Sex'].describe(),'\n')
print(titanic['Sex'].nbytes,'\n')

inicio = timeit.default_timer()
print(titanic['Sex'] == 'Male','\n')
fim = timeit.default_timer()
print(fim - inicio,'\n')