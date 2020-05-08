# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 2017

@author: Leonardo
"""
from sklearn import datasets

diabetes = datasets.load_diabetes()
print(diabetes.data)
print(diabetes.target)
print(diabetes.DESCR)

x, y = diabetes.data, diabetes.target

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=42)

print(len(x_train))
print(len(x_test))

from sklearn.neighbors import KNeighborsRegressor
knn= KNeighborsRegressor(n_neighbors=20, p=2)
knn.fit(x_train, y_train)
output = knn.predict(x_test)

print('Saída esperada: %f' %y_test[3])
print('Saída predita: %f' %output[3])


from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, output))