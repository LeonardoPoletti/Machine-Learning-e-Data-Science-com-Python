# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:23:00 2017

@author: Leonardo
"""

import pandas as pd
import numpy as np

df = pd.read_csv('primary-results.csv')
print(df.head())
print('\n', '##########################################################')
print('\n',len(df))
print('\n', '##########################################################')
print('\n',df.groupby('candidate'))
print('\n', '##########################################################')
print('\n', df.groupby('candidate').aggregate({'votes': [min, np.mean, max]}))
print('\n', '##########################################################')
print('\n', df[df['votes'] == 590502])
print('\n', '##########################################################')
print('\n', df.loc[df['votes'] == 590502])
print('\n', '##########################################################')
print('\n', df.groupby('candidate').aggregate({'fraction_votes': [min, np.mean, max]}))
print('\n', '##########################################################')
print('\n', df.loc[(df['fraction_votes'] == 1) & (df['candidate'] == 'Hillary Clinton')])

def fraction_votes_filter(x):
    return x['votes'].sum() > 1000000

print('\n', df.groupby('state').filter(fraction_votes_filter))

print('\n', '##########################################################')

print('\n', df[df['state_abbreviation'] == 'AL']['votes'].sum())
print('\n', '##########################################################')

print('\n', df.groupby(['state_abbreviation', 'candidate'])['votes'].sum())
print('\n', '##########################################################')
