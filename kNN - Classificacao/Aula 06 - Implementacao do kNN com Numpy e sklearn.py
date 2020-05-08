# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 2017

@author: Leonardo

Dataset = https://archive.ics.uci.edu/ml/datasets/Balance+Scale

Attribute Information:

1. Class Name: 3 (L, B, R) 
2. Left-Weight: 5 (1, 2, 3, 4, 5) 
3. Left-Distance: 5 (1, 2, 3, 4, 5) 
4. Right-Weight: 5 (1, 2, 3, 4, 5) 
5. Right-Distance: 5 (1, 2, 3, 4, 5)

São 625 exemplos, 4 atribuotos e 3 possíveis classes.
Onde tem "L" coloqiei 1, onde tem "B" coloquei 2, onde tem "R" coloquei 3
"""

import numpy as np
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# x são as entradas e y são as saídas
x = np.genfromtxt('balance-scale.data', delimiter=',', usecols=(1,2,3,4))
y = np.genfromtxt('balance-scale.data', delimiter=',', usecols=(0))

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3, random_state=42)

'''
print(len(x_teste))
print(len(x_treino))
print(x_teste[0])
print(y_teste[0])
'''

knn = KNeighborsClassifier(n_neighbors=17, p=2)
knn.fit(x_treino, y_treino)
labels = knn.predict(x_teste)



print('Total de treinamento: %d' %(len(x_treino)))
print('Total de testes: %d' %(len(x_teste)))
print('Total de acertos: %d' % np.sum(labels == y_teste))
print('Total de acertos: %d' % (labels == y_teste).sum())
print('Procentagem de acertos: %.2f%%' %(100 * (labels == y_teste).sum() / len(x_teste)))

print('Score: %f' % knn.score(x_teste, y_teste))
print('Score: %f' % np.mean(labels ==  y_teste))














