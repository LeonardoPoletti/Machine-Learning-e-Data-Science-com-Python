# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:32:11 2017

@author: Leonardo
"""

import pandas as pd

df = pd.DataFrame(
        [
                ['PE', 'Pernanbuco', 'Recife'],
                ['RJ', 'Rio de Janeiro', 'Rio de Janeiro'],
                ['PB', 'Paraíba', 'João Pessoa'],
                ['SP', 'São Paulo', 'São Paulo'],
                ['MG', 'Minas Gerais', 'Belo Horizonte'],
                ['CE', 'Ceará', 'Fortaleza'],
                ['AC', 'Acre', 'Rio Branco'],
                ['MA', 'Maranhão', 'São Luís'],
                ['RN', 'Rio Grande do Norte', 'Natal'],
                ['PR', 'Paraná', 'Curitiba'],
                ['RS', 'Rio Grande do Sul', 'Porto Alegre']
        ],columns = ['Sigla', 'Nome', 'Capital']
)

print(df,'\n')

print(df['Sigla'],'\n')
print(df.index,'\n')


#print(df.ix[0],'\n')
print(df.loc[3],'\n')
print(df.iloc[5],'\n')

#print(df.ix[:2],'\n')
print(df.iloc[:2],'\n')

df.index = pd.Index([1,2,3,4,5,6,7,8,9,10,11])

print(df,'\n')

df.index = df['Sigla']
print(df,'\n')

del df['Sigla']

print(df,'\n')