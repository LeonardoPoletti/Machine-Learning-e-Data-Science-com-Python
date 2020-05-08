# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:31:10 2017

@author: Leonardo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import matplotlib.dates as dates
import datetime as dt
#import locale
import time

df = pd.read_csv('ppz-jan-fev-2017.csv')

print(df.tail())

def to_date(value):
    return dt.datetime(2017, 1, 1) + dt.timedelta(hours=value)

df['date'] = df['hour'].apply(to_date)
print('\n',df.head())
print('\n',df.tail())

del df['hour']
print('\n',df.head())
print('\n',df.tail())

df.set_index(['date'], inplace=True)
print('\n',df.head())
print('\n',df.tail())

#locale.setlocale(locale.LC_ALL, 'pt_BR')

fig, ax = plt.subplots()
ax.plot_date(df.index.to_pydatetime(), df['views'], 'b-')

ax.xaxis.set_minor_locator(dates.DayLocator(bymonthday=range(5,32,5), interval =2 ))
ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))
ax.xaxis.grid(True, which='minor')
ax.yaxis.grid()

ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))

plt.tight_layout()
plt.show()

time.sleep(1000)