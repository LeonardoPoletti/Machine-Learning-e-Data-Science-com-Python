# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 23:10:08 2017

@author: Leonardo
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('iris.data', delimiter=',', usecols=(0,1,2,3))
#print(data)

print(len(data))

print(data[:,0],'\n') #valores da primeira coluna
print(data[:50,0])#somete as 50 primeiras

plt.plot(data[:50,0], c ='red', ls=':', marker='s', ms=8, label= 'Comp. Sépala Iris-Setosa')
plt.plot(data[50:100,0], c ='black', ls=':', marker='o', ms=8, label= 'Comp. Sépala Iris-Versicolor')
plt.plot(data[100:150,0], c ='green', ls=':', marker='^', ms=8, label= 'Comp. Sépala Iris-Virginica')
plt.legend()
plt.show()