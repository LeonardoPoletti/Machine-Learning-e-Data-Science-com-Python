# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:27:00 2017

@author: Leonardo
"""

import pandas as pd

copacabana = pd.read_csv('copacabana.csv', delimiter=';')
"""
print(copacabana.columns,'\n')
print('#################################################################')
print(copacabana['Quartos'].describe(),'\n')
print('#################################################################')
print(copacabana['Quartos'] >5,'\n')
print('#################################################################')
print(copacabana.loc[copacabana['Quartos'] == 6],'\n')
print('#################################################################')
print(copacabana.loc[copacabana['Quartos'] == 5],'\n')
print('#################################################################')
print(copacabana['AreaConstruida'] * copacabana['VAL_UNIT'])
print('#################################################################')
"""
copacabana['Total'] = copacabana['AreaConstruida'] * copacabana['VAL_UNIT']
print(copacabana['Total'].describe())
