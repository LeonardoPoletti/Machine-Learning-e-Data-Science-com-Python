# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 2017

@author: Leonardo
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time


titanic = pd.read_csv('titanic.csv')
print(titanic.head())

#print('\n',titanic['Sex'].value_counts())
#print('\n',titanic['Survived'].value_counts())

titanic['Sex'].value_counts().plot(kind='bar')
plt.show()
titanic['Survived'].value_counts().plot(kind='bar')
plt.show()

print(titanic.groupby('Survived')['Sex'].value_counts().plot(kind='bar'))
plt.show()

time.sleep(1000)
