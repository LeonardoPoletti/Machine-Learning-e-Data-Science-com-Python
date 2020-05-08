# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 2017

@author: Leonardo
"""

with open('balance-scale.txt') as entrada, open('balance-scale.data', 'w') as saida:
    for linha in entrada:
        linha = linha.replace('B', '2').replace('L', '1').replace('R', '3')            
        
        saida.writelines(linha)

entrada.close()
saida.close()



#teste

entradas, saidas = [], []

with open('balance-scale-correto.data', 'r') as f:
    for linha in f.readlines():
        atrib = linha.replace('\n', '').split(',')
        entradas.append([int(atrib[1]), int(atrib[2]), int(atrib[3]), int(atrib[4])])
        saidas.append(int(atrib[0]))
        

print(entradas)
print(saidas)
        
        
        
        