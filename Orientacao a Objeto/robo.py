# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 16:07:45 2017

@author: Leonardo
"""

#O programa ira percorrerer uma matriz 10x10 e receberá recompensas. 
#Utilzando Orientação a Objetos OO

import point as p
#import reward as r

class Robo(p.Point):
    
    def __init__(self, x, y):
         super(Robo, self).__init__(x,y)

    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('Movimento Proibido')
        
    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('Movimento Proibido')
    
    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('Movimento Proibido')
        
    def move_right(self):
        if self.x < 10:
            self.x = self.x + 1
        else: 
            print('Movimento Probido')

    def check_reward(robot, rewards):
        ok = False
        for reward in rewards:
            if reward.x == robot.x and reward.y == robot.y:
                print('O robô achou a recompensa: %s' % reward.name)
               # ok = True
        return ok
                