# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 2017

@author: Leonardo
"""

import pandas as pd

alunos1 = pd.DataFrame(
    {
        'nome': ['Maria', 'Sofia'],
        'nota': [8, 9]
    }
)

alunos2 = pd.DataFrame(
    {
        'nome': ['João', 'Pedro', 'Maria'],
        'cod': [1, 2, 3]
    }
)

alunos_total = pd.merge(alunos1, alunos2, how='inner')
print(alunos_total,'\n')

alunos_total = pd.merge(alunos1, alunos2, how='outer')
print(alunos_total,'\n')

alunos_total = pd.merge(alunos1, alunos2, how='left')
print(alunos_total,'\n')

alunos_total = pd.merge(alunos1, alunos2, how='right')
print(alunos_total,'\n')