# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:42:05 2017

@author: Leonardo
"""

import numpy as np
import matplotlib.pyplot as plt

salarios_marcos = np.array([100, 200, 400, 300])
salarios_gileno = np.array([50, 300, 500, 450])
"""
plt.plot(salarios_marcos, c='Black', ls='--', marker='s', ms = 5, label = 'Salários Marcos')
plt.plot(salarios_gileno, c='Red', ls='--', marker='s', ms = 5, label = 'Salários Gileno')
plt.show()
"""
"""
plt.plot(salarios_marcos, c='Black', ls='--', marker='s', ms = 5, label = 'Salários Marcos')
plt.plot(salarios_gileno, c='Red', ls='--', marker='^', ms = 5, label = 'Salários Gileno')
plt.legend()
plt.show()
"""
"""
plt.plot(salarios_marcos, c='Black', ls='--', marker='s', ms = 5, label = 'Salários Marcos')
plt.plot(salarios_gileno, c='Red', ls='--', marker='^', ms = 5, label = 'Salários Gileno')
plt.legend(loc = 'upper left')
plt.show()
"""
salarios_pedro = ([200, 150, 300, 700])

plt.plot(salarios_marcos, c='Black', ls='--', marker='s', ms = 5, label = 'Salários Marcos')
plt.plot(salarios_gileno, c='Red', ls='--', marker='^', ms = 5, label = 'Salários Gileno')
plt.plot(salarios_pedro, c='Green', ls='--', marker='o', ms = 5, label = 'Salários Pedro')
plt.legend(loc = 'upper left')
plt.show()




