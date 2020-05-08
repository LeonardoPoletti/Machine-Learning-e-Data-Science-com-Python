# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 2017

@author: Leonardo
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

train = pd.read_csv('shoe-train.csv')
test = pd.read_csv('shoe-test.csv')

cols = ['shoe size', 'height']
cols2 = ['class']

x_train = train.as_matrix(cols)
y_train = train.as_matrix(cols2)
x_test = test.as_matrix(cols)
y_test = test.as_matrix(cols2)

knn = KNeighborsClassifier(n_neighbors=3, weights='distance')
knn.fit(x_train, y_train.ravel())
output = knn.predict(x_test)

corret = 0
for i in range(len(output)):
    if y_test[i][0] == output[i]:
        corret += 1
    
print(corret/len(output))

