# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 18:09:19 2017

@author: Leonardo
"""
import point as p

class Reward(p.Point):
    
    def __init__(self, x, y, name):
        super(Reward, self).__init__(x,y)
        self.name = name
    
    def __str__(self):
        return '<%s, %s>: %s' % (self.x, self.y, self.name)
    
    def __repr__(self):
        return 'Reward %s' % str(self)