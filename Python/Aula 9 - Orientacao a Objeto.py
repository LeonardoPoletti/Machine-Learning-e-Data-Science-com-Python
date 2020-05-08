# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 23:50:03 2017

@author: Leonardo
"""

class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def imprimir_nome(self):
        print(self.nome)
    
p = Pessoa ('Leonardo', 26)
print(type(p))

p.imprimir_nome()
print(p.idade)

############################################################

class Conta:
    
    def __init__(self, cliente, numero):
        self.cliente = cliente
        self.numero = numero
        
class ContaEspecial(Conta):
    
    def __init__(self, cliente, numero, limite = 0):
        Conta.__init__(self, cliente, numero)
        self.limite = limite
        
conta = ContaEspecial('Leonardo', '123', 1000)
print(conta.limite)


        
