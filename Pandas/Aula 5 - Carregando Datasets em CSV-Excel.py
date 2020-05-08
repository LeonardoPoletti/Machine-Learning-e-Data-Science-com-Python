# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 00:04:00 2017

@author: Leonardo
"""

import pandas as pd

#help(pd.read_csv)

copacabana = pd.read_csv('copacabana.csv', delimiter=';')
#print(copacabana)
print(copacabana.head())

copacabana_excel = pd.read_excel('copacabana_.xlsx')
print(copacabana_excel.head())