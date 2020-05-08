# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17  2017

@author: Leonardo
"""

from sklearn import datasets

iris = datasets.load_iris()
print(iris.feature_names)
print(iris.target_names)
print(len(iris.data))

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

X, y = iris.data, iris.target

mlp = MLPClassifier(solver='adam', alpha=0.0001, hidden_layer_sizes=(5,), 
                    random_state=1, learning_rate='constant', 
                    learning_rate_init=0.01, max_iter=500, activation='logistic',
                    momentum=0.9, verbose='True', tol=0.001)

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.3, random_state=1)
mlp.fit(X_treino, y_treino)
saidas = mlp.predict(X_teste)

print('---------------------------------------------------')

print('Saída da rede:\t', saidas)
print('Saída desejada:\t', y_teste)
print('---------------------------------------------------')

print('Score: ', (saidas == y_teste).sum() / len(X_teste))
print('Score:', mlp.score(X_teste, y_teste))
