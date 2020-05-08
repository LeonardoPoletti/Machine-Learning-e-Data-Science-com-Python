# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 16:26:47 2017

@author: Leonardo
"""

#O programa ira percorrerer uma matriz 10x10 e receberá recompensas. 
#Utilzando Orientação a Objetos OO

import robo as r
import reward as re
import random
#import robo3d as r3d


rw1_random = re.Reward(random.randint(0, 10), random.randint(0, 10), 'Bateria')
rw2_random = re.Reward(random.randint(0, 10), random.randint(0, 10), 'Oleo')
rw3_random = re.Reward(random.randint(0, 10), random.randint(0, 10), 'Munição')

rewards = [rw1_random, rw2_random, rw3_random]

robot = r.Robo(random.randint(0, 10), random.randint(0, 10))
print(robot)
print(rewards)
 
for i in range(10):
    moviment = input('Digite up, down, left ou right para o movimento: ')
    if moviment == 'up':
        robot.move_up()
    elif moviment == 'down':
        robot.move_down()
    elif moviment == 'left':
        robot.move_left()
    elif moviment == 'right':
        robot.move_right()
    else:
        print('Movimento invalido')
        continue
    print(robot)
    r.Robo.check_reward(robot, rewards)



'''  Codigo Teste
reward1 = re.Reward(1, 1, 'Moeda de Ouro')
reward2 = re.Reward(4, 5, 'Oleo')
reward3 = re.Reward(6, 3, 'Bateria')

robot1 = r.Robo(4, 5)
print(robot1.x)
print(robot1.y)

rewards = [reward1, reward2, reward3]

r.Robo.check_reward(robot1, rewards)

robot1.move_down()
robot1.move_down()
robot1.move_right()
robot1.move_right()

print(robot1.x)
print(robot1.y)

r.Robo.check_reward(robot1, rewards)
'''