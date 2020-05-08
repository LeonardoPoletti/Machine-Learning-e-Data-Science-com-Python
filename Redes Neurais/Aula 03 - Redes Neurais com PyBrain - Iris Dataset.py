# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:08:55 2017

@author: Leonardo
"""
"""
Iris-Setosa: 0
Iris-Versicolor: 1
Iris-Virginica: 2
"""

import numpy as np

entradas = np.genfromtxt('iris.data', delimiter=',', usecols=(0,1,2,3))
saidas = np.genfromtxt('iris.data', delimiter=',', usecols=(4))

print(len(entradas))
print(len(saidas))
print('--------------------------')
# Mostrando as amostras que são Iris-Setosa
print(entradas[:5])
print(saidas[:5])
print('--------------------------')
# Mostrando as amostras que são Iris-Versicolor
print(entradas[50:55])
print(saidas[50:55])
print('--------------------------')
# Mostrando as amostras que são Iris-Virginica
print(entradas[-5:])
print(saidas[-5:])
print('--------------------------')
print('--------------------------')

# 105 amostras para treino sendo 35 para cada classe
entradas_treino = np.concatenate((entradas[:35], entradas[50:85], entradas[100:135]))
saidas_treino = np.concatenate((saidas[:35], saidas[50:85], saidas[100:135]))
print(len(entradas_treino))
print(len(saidas_treino))
print('--------------------------')

entradas_teste = np.concatenate((entradas[35:50], entradas[85:100], entradas[135:]))
saidas_teste = np.concatenate((saidas[35:50], saidas[85:100], saidas[135:]))
print(len(entradas_teste))
print(len(saidas_teste))
print('--------------------------')

from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

treinamento = SupervisedDataSet(4, 1)
for i in range(len(entradas_treino)):
    treinamento.addSample(entradas_treino[i], saidas_treino[i])
print(len(treinamento))
print(treinamento.indim)
print(treinamento.outdim)
print('--------------------------')

# Construindo a rede
rede = buildNetwork(treinamento.indim, 2, treinamento.outdim, bias=True)
trainer = BackpropTrainer(rede, treinamento, learningrate=0.01, momentum=0.7)

# Treinando a rede
for epoca in range(1000):
    trainer.train()
    
# Testando a rede
teste = SupervisedDataSet(4, 1)
for i in range(len(entradas_teste)):
    teste.addSample(entradas_teste[i], saidas_teste[i])
trainer.testOnData(teste, verbose=True)