# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 2017

@author: Leonardo
"""
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
print(cancer.keys())
print('--------------------------------------------------------------------------------------')

print(cancer.feature_names)
print(cancer.target_names)
print(len(cancer.data))
print(cancer['data'].shape)
print('--------------------------------------------------------------------------------------')

X, y = cancer['data'], cancer['target']
print(len(X))
print(len(y))
print('--------------------------------------------------------------------------------------')


from sklearn.model_selection import train_test_split

X_train, X_teste, y_train, y_teste = train_test_split(X, y)
print(len(X_train))
print(len(X_teste))
print('--------------------------------------------------------------------------------------')

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_teste = scaler.transform(X_teste)

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(50, 50, 50),max_iter=500)
mlp.fit(X_train, y_train)

print(mlp)
print('--------------------------------------------------------------------------------------')

predictions = mlp.predict(X_teste)


print('Saída da rede:\t', predictions)
print('Saída desejada:\t', y_teste)
print('--------------------------------------------------------------------------------------')

print('Score: ', (predictions == y_teste).sum() / len(X_teste))
print('Score:', mlp.score(X_teste, y_teste))
print('--------------------------------------------------------------------------------------')

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_teste, predictions))
print('--------------------------------------------------------------------------------------')
print(classification_report(y_teste, predictions))
print('--------------------------------------------------------------------------------------')

print(mlp.coefs_)
print(mlp.intercepts_)