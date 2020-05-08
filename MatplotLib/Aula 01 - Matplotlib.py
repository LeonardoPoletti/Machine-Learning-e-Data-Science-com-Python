# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 2017

@author: Leonardo
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(1, 10, 100)
#print(x)
'''
plt.plot(x, np.sin(x))
plt.show()

plt.plot(x, np.sin(x), 'r')
plt.show()

plt.plot(x, np.sin(x), 'r--')
plt.show()
'''
fig = plt.figure()
plt.plot(x, np.sin(x), 'r--')
fig.savefig('sin-01.png')

