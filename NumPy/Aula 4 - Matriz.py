# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:54:33 2017

@author: Leonardo
"""

import numpy as np

joao_pts = [20, 30, 40, 15]
pedro_pts = [100, 24, 48, 23]
maria_pts = [92, 22, 34, 12]
marcus_pts =[12, 34, 12, 43] 
   
pontos = np.array([joao_pts, pedro_pts, maria_pts, marcus_pts])
print(pontos)
print('####################')
print(pontos[0])
print('####################')
print(pontos[1][0])
print('####################')

my_data = np.arange(0,20)
print(my_data)
mat1 = np.reshape(my_data, (5,4))
print(mat1) 
print('####################')
print(mat1[2,2]) 
print(pontos.item(5))

print('####################')
m1 = ['python', 'eh', 'legal'] 
m2 = ['guido', 'van', 'rossum'] 
m3 = [10, 20, 30]

print([m1, m2, m3])
print('\n')
print(np.array([m1, m2, m3]))
      