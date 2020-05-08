# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 16:32:37 2017

@author: Leonardo
"""

#O programa ira percorrerer uma matriz 10x10 e receberá recompensas. 
#Utilzando Orientação a Objetos OO
import robo as r

class Robo3D(r.Robo):
    
    def __init__(self, x, y, z):
        super(Robo3D, self).__init__(x, y)
        self.z = z