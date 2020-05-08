# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7  2017

@author: Leonardo
"""

import math
import numpy as np

v1 = [1.2, 2, 3.8, 4.5]
v2 = [0.5, 4.5, 9.6, 3.4]

def dist_euclidiana_np(v1, v2):
    v1, v2 = np.array(v1), np.array(v2)
    diff = v1 - v2
    quad_dist = np.dot(diff, diff)
    return math.sqrt(quad_dist)
  

def dist_manhattan(v1, v2):
    v1, v2 = np.array(v1), np.array(v2)
    diff = v1 - v2
    sum_dist = np.sum(diff)
    return np.abs(sum_dist)
 
print('%.2f' % dist_euclidiana_np(v1, v2))   
print('%.2f' % dist_manhattan(v1, v2)) 