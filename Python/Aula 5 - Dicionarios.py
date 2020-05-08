# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 21:41:03 2017

@author: Leonardo
"""

d = {'Leonardo':27, 'Ingrid':26, 'Maria':28, 'Pedro':24}
print(d)
print(d['Leonardo'])

d['Ingrid'] = 27
print(d['Ingrid'])

d['Manoel'] = 30
print(d)

for k in d:
    print(d[k], end=' ')
    
print()
print()
print()

print(d.items())
print(d.keys())
print(d.values())
print('Ingrid' in d)
print('Josefa' in d)