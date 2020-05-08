# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 21:55:53 2017

@author: Leonardo
"""

def somar(n1, n2):
    return n1 + n2

print(somar(1,3))
print(somar(4,6))


def imprimir():
    print('Viva Las Vegas')
    print('Viva')
    
imprimir()

def eh_par(x):
    return x % 2 == 0

print(eh_par(10))
print(eh_par(11))

def foo(*args):
    return sum(*args)

print(foo([1,2,3,4,5,6,7,8,9]))
print(foo([1,3]))

imprimir = print
imprimir('Hello Word')

#############################################################

#Fatorial

def fat(n):
    if n == 0 or n == 1:
        return 1
    return n * fat(n - 1)

print(fat(5))

def imprimir_nome(nome = 'desconhecido'):
    print(nome)
    
imprimir_nome()

def somar(x, y, z, f):
    return x + f(y, z)

def f(n1, n2):
    return n1 + n2

print(somar(10, 20,30, f))

a = lambda x: x*2
print(a(4))
print(a(10))



























