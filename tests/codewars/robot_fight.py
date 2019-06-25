#!/usr/bin/python3.5

import itertools
def fight(robot1, robot2, tactics):
    for t1, t2 in itertools.zip_longest(robot1.tactics, robot2.tactics):
        if robot1.speed >= robot2.speed:
            if t1: robot2.health -= getattr(tactics, t1)
            if robot2.health <= 0:
                return '{} has won the fight.'.format(robot1.name)
            if t2: robot1.health -= getattr(tactics, t2)
            if robot2.health <= 0:
                return '{} has won the fight.'.format(robot2.name)
        else:
            if t2: robot1.health -= getattr(tactics, t2)
            if robot1.health <= 0:
                return '{} has won the fight.'.format(robot2.name)
            if t1: robot2.health -= getattr(tactics, t1)
            if robot2.health <= 0:
                return '{} has won the fight.'.format(robot1.name)
    if robot1.health > robot2.health: return '{} has won the fight.'.format(robot1.name)
    elif robot2.health > robot1.health: return '{} has won the fight.'.format(robot2.name)
    return 'The fight was a draw.'
    
def fight_dict(robot1, robot2, tactics):
    for t1, t2 in itertools.zip_longest(robot1['tactics'], robot2['tactics']):
        # print(t1, t2)
        
        if robot1['speed'] >= robot2['speed']:
            if t1: robot2['health'] -= tactics[t1]
            if robot2['speed'] <= 0: return '{} has won the fight.'.format(robot1['name'])
            if t2: robot1['health'] -= tactics[t2]
            if robot2['health'] <= 0: return '{} has won the fight.'.format(robot2['name'])
        else:
            if t2: robot1['health'] -= tactics[t2]
            if robot1['health'] <= 0: return '{} has won the fight.'.format(robot2['name'])
            if t1: robot2['health'] -= tactics[t1]
            if robot2['health'] <= 0: return '{} has won the fight.'.format(robot1['name'])
    if robot1['health'] > robot2['health']: return '{} has won the fight.'.format(robot1['name'])
    elif robot2['health'] > robot1['health']: return '{} has won the fight.'.format(robot2['name'])
    else: return 'The fight was a draw.'

class robot_1 :
  name = "Rocky"
  health = 200
  speed = 20
  tactics = ["punch", "punch", "laser", "missile"]

class robot_2 :
   name = "Missile Bob"
   health = 100
   speed = 21
   tactics = ["missile", "missile", "missile", "missile"]

class tactics :
   punch = 20
   laser = 30
   missile = 35

robot_1_d = {'name': 'Rocky',
    'health': 519,
    'speed': 87,
    'tactics': ['punch', 'missile', 'punch', 'punch', 'punch', 'laser', 'laser', 'missile', 'missile', 'laser']}

robot_2_d = {'name': 'Missile Bob',
    'health': 504,
    'speed': 42,
    'tactics': ['missile', 'punch', 'punch', 'laser', 'laser', 'laser', 'punch', 'laser', 'missile', 'laser']}

tactics_d = {'punch': 20,
    'laser': 30,
    'missile': 35}
# print(getattr(tactics, 'punch'))
# print(fight(robot_1, robot_2, tactics))
print(fight_dict(robot_1_d, robot_2_d, tactics_d))