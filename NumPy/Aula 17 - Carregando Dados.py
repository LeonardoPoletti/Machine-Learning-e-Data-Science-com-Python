# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:35:01 2017

@author: Leonardo
"""
"""
texto = '''Valores1   Valores2    Valores3
0.1212     0.842       0.3672
0.104      0.5422      0.34551
0.5661     0.932       MISSING
0.762      0.847361    0.1538
'''

with open ('dados2.txt', 'w') as f:
    f.write(texto)
"""

import numpy as np

val1, val2, val3 = np.loadtxt('dados.txt', skiprows=1, unpack=True)

print(val1)
print(val2)
print(val3)
print()
my_arry = np.genfromtxt('dados2.txt', skip_header=1, filling_values=1)

print(my_arry)
