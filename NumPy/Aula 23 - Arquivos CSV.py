# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 23:04:44 2017

@author: Leonardo
"""
import numpy as np

valores = np.genfromtxt("arquivo.csv", delimiter=";", skip_header=1)

print(valores)





"""
texto = '''Valores1;Valores2;Valores3
10;20;30
40;50;60
70;80;90
34;54;23
'''

with open ('arquivo.csv', 'w') as f:
    f.write(texto)
"""