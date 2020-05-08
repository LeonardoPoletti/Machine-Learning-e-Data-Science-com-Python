# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 2017

@author: Leonardo
"""

import numpy as np
from sklearn import neighbors, datasets

iris = datasets.load_iris()

x = iris.data
#print(x)
#print(len(x))

y = iris.target
#print(y)
#print(iris.target_names)

knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(x,y)

knn.predict(x)

acuracia = knn.score(x,y)
print(acuracia)