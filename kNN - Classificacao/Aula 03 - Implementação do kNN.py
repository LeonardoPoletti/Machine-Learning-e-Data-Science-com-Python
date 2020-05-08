# -*- coding: utf-8 -*-
"""
Created on Fri Sep 2017

@author: Leonardo

Implementação do kNN
dataset: https://archive.ics.uci.edu/ml/datasets/Haberman%27s+Survival
Descrição do dataset: sobrevivência de pacinetes submetidos a cirugia de câncer de mama
"""

#Lista de amostras
amostras =[]

with open('haberman.data', 'r') as f:
    for linha in f.readlines():
        atrib = linha.replace('\n', '').split(',')
        amostras.append([int(atrib[0]), int(atrib[1]),
                        int(atrib[2]), int(atrib[3])])


def info_dataset(amostras, verbose = True):
    if verbose:
        print('Total de amostras: %d' % len(amostras))
    rotulo1, rotulo2 = 0, 0
    for amostra in amostras:
        if (amostra[-1] == 1):
            rotulo1 += 1
        else:
            rotulo2 += 1
    if verbose:
        print('Total rotulo 1: %d' % rotulo1)
        print('Total rotulo 2: %d' % rotulo2)
    return [len(amostras), rotulo1, rotulo2]

#info_dataset(amostras)
 
#Variavel para defenir a porcentagem que sera usado para treinamento

p = 0.6

#Usa-se '_' quando não deseja pegar tal informação vinda de uma função
_, rotulo1, rotulo2 = info_dataset(amostras, verbose=False)
          
#Dividir em duas listas as amostras
treinamento, teste = [], []

#Calcular a porcentagem usada para cada um.
max_rotulo1, max_rotulo2 = int(p * rotulo1), int(p * rotulo2)

#pasando as informações para as listas
total_rotulo1, total_rotulo2 = 0, 0
for amostra in amostras:
    if(total_rotulo1 + total_rotulo2 < max_rotulo1 + max_rotulo2):
        treinamento.append(amostra)
        if(amostra[-1] == 1) and (total_rotulo1 < max_rotulo1):
            total_rotulo1 += 1
        else:
            total_rotulo2 += 1
    else:
        teste.append(amostra)
'''       
print(max_rotulo1,'\n')
print(max_rotulo2,'\n')       
print(info_dataset(treinamento),'\n')
print(info_dataset(teste))   
'''
 
#Codigo do kNN

import math

def dist_euclidiana(v1, v2):
    dim, soma = len(v1), 0
    #sera -1 pois o ultimo atributo é a saida (1 ou 2)
    for i in range(dim - 1):
        soma += math.pow(v1[i] - v2[i],2)
    return math.sqrt(soma)


def knn (treinamento, nova_amostra, K):
    dists, tam_treino = {}, len(treinamento)
    # calcula a distância euclidiana da nova amostra para
    # todos os outros exemplos do conjunto de treinamento
    for i in range(tam_treino):
        d = dist_euclidiana(treinamento[i], nova_amostra)
        dists[i] = d
        
    # obtém as chaves (índices) dos k-vizinhos mais proxímos
    k_vizinhos = sorted(dists, key=dists.get)[:K]
    
    #votação majoritária
    qtd_rotulo1, qtd_rotulo2 = 0, 0
    for indice in k_vizinhos:
        if treinamento[indice][-1] == 1:
            qtd_rotulo1 +=1
        else:
            qtd_rotulo2 += 1
    
    if qtd_rotulo1 > qtd_rotulo2:
        return 1
    else:
        return 2
    

#K = 13 = raiz quadrada do treimnamento
acertos, K = 0, 20
for amostra in teste:
    classe = knn(treinamento, amostra, K)
    if amostra[-1] == classe:
        acertos += 1
        
print('Total de treinamento: %d' % len(treinamento))
print('Total de testes: %d' % len(teste))
print('Total de acertos: %d' % acertos)
print('Porcentagem de acertos: %.2f%%' % (100 * acertos / len(teste)))