# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1  2017

@author: Leonardo
"""

import matplotlib.pyplot as plt
import pandas as pd
#import seaborn
import time
import mplleaflet

df = pd.read_csv('copacabana_lat_lng.csv')

plt.scatter(df['lng'], df['lat'], marker='.')
mplleaflet.display()
plt.show()
mplleaflet.show()

print('ii')



