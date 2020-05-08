# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 2017

@author: Leonardo
"""

#Classificação com Pybrain - XOR de 3 dimensões
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

dataset = SupervisedDataSet(3, 1)

dataset.addSample([0,0,0], [0])
dataset.addSample([0,0,1], [1])
dataset.addSample([0,1,0], [1])
dataset.addSample([0,1,1], [0])
dataset.addSample([1,0,0], [1])
dataset.addSample([1,0,1], [0])
dataset.addSample([1,1,0], [0])
dataset.addSample([1,1,1], [1])

#network = buildNetwork(dataset.indim, 6, 6, dataset.outdim, bias=True)
network = buildNetwork(dataset.indim, 3, dataset.outdim, bias=True)
trainer = BackpropTrainer(network, dataset, learningrate=0.01, momentum=0.9)

for i in range(1500):
    trainer.train()

teste = SupervisedDataSet(3,  1)    
teste.addSample([0,0,0], [0])
teste.addSample([0,0,1], [1])
teste.addSample([0,1,0], [1])
teste.addSample([0,1,1], [0])
teste.addSample([1,0,0], [1])
teste.addSample([1,0,1], [0])
teste.addSample([1,1,0], [0])
teste.addSample([1,1,1], [1])

trainer.testOnData(teste, verbose=True)