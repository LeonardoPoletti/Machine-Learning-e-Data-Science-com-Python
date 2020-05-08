# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:29:45 2017

@author: Leonardo
"""

import numpy as np
import matplotlib.pyplot as plt
 
salario = np.array([100, 200, 300, 500, 400, 150])
 
#plt.plot(salario)

#plt.plot(salario, c='Black')

#plt.plot(salario, c='Black', ls= '--')

plt.plot(salario, c='Black', ls='--', marker='s', ms=5)
plt.show()



