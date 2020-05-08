# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 21:25:42 2017

@author: Leonardo
"""

s = set()
s.add(10)
s.add(20)
s.add(30)
s.add(10)

print(s, type(s))

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(type(s1), type(s2))

uniao = s1.union(s2)
print(uniao)

inter = s1.intersection(s2)
print(inter)

diff = s1.difference(s2)
print(diff)

lista = [1,2,3,4,4,4,4,4,5,5,5,6,6,6,7,7,7]
s = set(lista)
print(s)