# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 22:34:48 2017

@author: Leonardo
"""

import pandas as pd
from db import DB


database = DB(filename='logs.sqlite3', dbtype='sqlite')

print(database.tables,'\n')

log_df = database.tables.log
print(log_df,'\n')

log_df = database.tables.log.all()
print(log_df,'\n')

log_df = database.query('select * from log where user_id = 3')
print(log_df,'\n')

log_df = database.query('select * from log')
print(log_df)
