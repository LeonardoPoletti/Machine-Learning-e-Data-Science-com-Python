# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 2017

@author: Leonardo
"""
 
import pandas as pd
import matplotlib.pyplot as plt
import time
import seaborn

df = pd.read_csv('reported.csv')

#print(df.head())

df.fillna(0, inplace=True)

#print(df.head())
'''
plt.plot(df['Year'], df['crimes.total'], '-r')
plt.plot(df['Year'], df['crimes.person'], '-b')
plt.show()
'''
fig, ax = plt.subplots()
ax.plot(df['Year'], df['crimes.total'], '-r')
ax.plot(df['Year'], df['crimes.person'], '-b')
ax.legend(loc='upper left')
ax.set_ylabel('Quantity')
ax.set_xlabel('Year') 
ax.set_title('Crimes: Total x Person')
ax.set_xlim([df['Year'].min(), df['Year'].max()])
plt.plot()

print('1')
#time.sleep(1000)