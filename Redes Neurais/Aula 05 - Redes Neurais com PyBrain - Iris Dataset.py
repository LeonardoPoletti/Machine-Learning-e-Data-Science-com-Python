# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 2017

@author: Leonardo
"""

#Carregando os dados do Iris Sataset com skLearn
from sklearn import datasets

iris = datasets.load_iris()
#Obtendo as entradas e saídas
X, y = iris.data, iris.target
print(len(X))
print(len(y))

from pybrain.datasets.classification import ClassificationDataSet

datasets = ClassificationDataSet(4, 1, nb_classes=3) #nb_classes = numeros de saidas

# adicionando as amostras
for i in range(len(X)):
    datasets.addSample(X[i], y[i])
len(datasets)  
'''
print(datasets['input'])
print(datasets['target'])
'''

# psrticonando os dados para treinamento
train_data, part_data = datasets.splitWithProportion(0.6) #sera dividido em 60%
print('Quantidade para treino: %d' % len(train_data))

# dividindo os dados para teste e validação
test_data, val_data = part_data.splitWithProportion(0.5)
print('Quantidade para teste: %d' % len(test_data))
print('Quantidade para validação: %d' % len(val_data))

from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

net = buildNetwork(datasets.indim, 3, datasets.outdim)
trainer = BackpropTrainer(net, dataset=train_data, learningrate=0.01, momentum=0.1, verbose=True)

train_erros, val_erros = trainer.trainUntilConvergence(dataset=train_data, maxEpochs=100)

import matplotlib.pyplot as plt

plt.plot(train_erros, 'b', val_erros, 'r')
plt.show()
print(trainer.totalepochs)




# OUtra forma de treinar
trainer.trainOnDataset(train_data, 500)

out = net.activateOnDataset(test_data)
for i in range(len(out)):
    print('out: %f, correct: %f' % (out[i], test_data['target'][i] ))


