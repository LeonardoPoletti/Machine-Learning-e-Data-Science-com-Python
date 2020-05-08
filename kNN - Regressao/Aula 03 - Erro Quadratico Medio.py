# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 2017

@author: Leonardo
"""

'''
Valor estimado é o valor tirando de uma função
Valor real é o que esta preenchido em algum tabela ou no seu data set

Erro = y - y' -> Valor real menos o valor estimado (pred)

Quadrado dos erros -> pegue o erro e eleve ao quadrado

'''
from sklearn.metrics import mean_squared_error

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

print(mean_squared_error(y_true, y_pred))

y_true = [1, 2, 3, 4]
y_pred = [1, 2, 3, 4]

print(mean_squared_error(y_true, y_pred))

y_true = [0.9, 1.2, 3.4]
y_pred = [0.8, 1.3, 3.5]

print(mean_squared_error(y_true, y_pred))
