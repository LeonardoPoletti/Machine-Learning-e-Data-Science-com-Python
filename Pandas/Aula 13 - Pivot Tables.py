# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 2017

@author: Leonardo
"""

import pandas as pd
import numpy as np

primary_df = pd.read_csv('primary-results.csv')

print(primary_df['candidate'].unique(),'\n')
'''
print(pd.pivot_table(
    primary_df, index=['state', 'party', 'candidate'],
    values=['votes'],
    aggfunc={'votes':np.sum}
))
'''
primary_df['rank'] = primary_df.groupby(['county', 'party'])['votes'].rank(ascending=False)

#print('\n', primary_df[primary_df['county'] == 'Los Angeles'])

primary_df_gb = primary_df.groupby(['state', 'party', 'candidate']).sum()
del primary_df_gb['fips']
del primary_df_gb['fraction_votes']
primary_df_gb.reset_index(inplace=True)
#print('\n', primary_df_gb.head(14))

primary_df_gb['rank'] = primary_df_gb.groupby(['state', 'party'])['votes'].rank(ascending=False)

#print('\n', primary_df_gb.head(20))

print('\n',pd.pivot_table(
    primary_df_gb, index=['state', 'party', 'candidate'],
    values=['rank', 'votes']
))

print('\n', primary_df_gb[primary_df_gb['rank'] == 1]['candidate'].value_counts())
