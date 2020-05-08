# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 2017

@author: Leonardo
"""

import pandas as pd
from db import DB
import time

database = DB(filename='logs.sqlite3', dbtype='sqlite')

time.sleep(2)
print(database.tables)

log_df = database.tables.log.all()
print(log_df.head())
print('\n', log_df.dtypes)

log_df['date'] = pd.to_datetime(log_df['date'], format='%Y-%m-%d %H:%M:%S.%f')
print('\n', log_df.dtypes)
print('\n', log_df.head())

log_df.set_index(['date'], inplace=True)
print('\n', log_df.head())

#print('\n', log_df['2017'])
print('\n', log_df['2017-01-03 10:47'])

print('\n', log_df['2017-01-03 10:47' : '2017-01-03 10:51'])
