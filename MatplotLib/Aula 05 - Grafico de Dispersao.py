# -*- coding: utf-8 -*-
"""
Created on Tue Aug 2017

@author: Leonardo
"""
import matplotlib.pyplot as plt
import pandas as pd
import time

iris = pd.read_csv('iris_dataset.csv')
#print(df)

#plt.plot(iris['SepalLeagth'], iris['SepalWidth'])
#plt.show()
'''
plt.scatter(iris['PetalLeagth'], iris['PetalWidth'])
plt.show()
'''

#plt.scatter(iris['SepalLeagth'], iris['SepalWidth'], sizes= 10 * iris['PetalLeagth'] )
#plt.show()

def specie_color(x):
    if x == 'setosa':
        return 0
    elif x == 'versicolor':
        return 1
    return 2

iris['SpeciesNumber'] = iris['Species'].apply(specie_color)
print(iris.tail())

plt.scatter(
        iris['SepalLeagth'], iris['SepalWidth'], 
        sizes=10 * iris['PetalLeagth'],
        c=iris['SpeciesNumber'],
        cmap='viridis',
        alpha=0.4
    )
plt.show()

time.sleep(1000)