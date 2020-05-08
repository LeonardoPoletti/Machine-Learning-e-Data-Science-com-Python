# -*- coding: utf-8 -*-
"""
Created on Sun Sep 2017

@author: Leonardo

Implementação do kNN
dataset: https://archive.ics.uci.edu/ml/datasets/Haberman%27s+Survival
Descrição do dataset: sobrevivência de pacinetes submetidos a cirugia de câncer de mama
"""

from sklearn.neighbors import KNeighborsClassifier

entradas, saidas = [], []

with open('haberman.data', 'r') as f:
    for linha in f.readlines():
        #O split é para pegar cada amostra individualemnte, ela estão sendo separadas por 
        # ',' então a utilizaremos no split
        atrib = linha.replace('\n', '').split(',')
        #entrada é uma lista de listas
        entradas.append([int(atrib[0]), int(atrib[2])])
        saidas.append(int(atrib[3]))
        
p = 0.6 #Porcentagem dos dados para treinamento

limite = int(p * len(entradas))
knn = KNeighborsClassifier(n_neighbors=20)
knn.fit(entradas[:limite], saidas[:limite]) #treinamento
labels = knn.predict(entradas[limite:]) #teste

acertos, indice_label = 0, 0
 
for i in range(limite,len(entradas)): #para testar os acertos dos testes
    if labels[indice_label] == saidas[i]:
        acertos += 1
    indice_label +=1

print('Total de treinamento: %d' %limite)
print('Total de testes: %d' %(len(entradas) - limite))
print('Total de acertos: %d' % acertos)
print('Procentagem de acertos: %.2f%%' %(100 * acertos / (len(entradas) - limite)))