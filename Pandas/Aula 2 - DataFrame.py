# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:17:17 2017

@author: Leonardo
"""

import pandas as pd

df = pd.DataFrame(
        [['fchollet/keras', 11302], ['openai/universe', 4350], ['pandas-dev/pandas', 8168]])

print(df,'\n')

print(df.shape)

df = pd.DataFrame(
        [['fchollet/keras', 11302], ['openai/universe', 4350], ['pandas-dev/pandas', 8168]],
        columns = ['repository', 'stars'])

print(df,'\n')

print(df['stars'],'\n')
print(df['repository'],'\n')


print(df['stars'].mean(),'\n')
print(df['stars'].median(),'\n')


print(df.iloc[1],'\n')
print(df.iloc[1]['stars'],'\n')