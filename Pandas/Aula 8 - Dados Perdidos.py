# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:01:00 2017

@author: Leonardo
"""

import pandas as pd
import numpy as np

dados = {
    'nome': ['João', 'Maria', 'José', np.nan, 'Pedro', 'Judas', 'Tiago'],
    'sexo': ['M', 'F', 'M', np.nan, 'M', 'M', np.nan],
    'idade': [14, 13, np.nan, np.nan, 15, 13, 14],
    'nota': [4, 10, 7, np.nan, 8, 9, 7]
}

df = pd.DataFrame(dados)

print(df,'\n')

print(df.dropna(),'\n')

print(df.dropna(how='all'),'\n')

df['serie'] = np.nan
print(df,'\n')

print(df.dropna(how='all', axis=1),'\n')

print(df.dropna(thresh=3),'\n')

print(df['serie'].fillna('8'),'\n')

#df['serie'].fillna('8', inplace=True)
#print(df,'\n')

df['idade'].fillna(df['idade'].mean(), inplace=True)

print(df,'\n')

print(df[df['nome'].notnull() & df['sexo'].notnull()], '\n')



