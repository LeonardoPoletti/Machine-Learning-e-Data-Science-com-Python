# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 2017

@author: Leonardo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import time

estados = pd.read_csv('populacao_brasil.csv')
#print(estados)

estados['total'].hist()
plt.show()

fig, ax = plt.subplots()
plt.hist(estados['total'], bins=15, orientation='horizontal')
ax.ticklabel_format(style='plain')
plt.show()

estados['percent'] = estados['total'] / estados['total'].sum()
print(estados.head())
plt.pie(estados['percent'], labels=estados['estado'])
plt.show()

plt.pie(estados['percent'], labels=estados['estado'], autopct='%1.2f%%')
plt.show()


time.sleep(1000)