# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 18:11:24 2017

@author: Leonardo
"""

class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)