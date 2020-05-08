# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 2017

@author: Leonardo
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 100)


plt.plot(x, np.sin(x), 'b--')
plt.plot(x, np.cos(x), 'r--')

plt.show()


import seaborn as sns

x = np.linspace(1, 10, 100)

sns.set_style('white')
sns.set_style('ticks')

plt.plot(x, np.sin(x), 'b--')
plt.plot(x, np.cos(x), 'r--')

plt.show()

