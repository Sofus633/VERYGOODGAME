import time
from enemy import FlyGobelin
from fireball import FireBall
import pygame
from storage import *
def tri_selection(objects):
    for object in objects:
        if isinstance(object, FlyGobelin) or isinstance(object, FireBall):
            if object.hide == True:
                objects.remove(object)
    for i in range(len(objects)):
        mini = i
        for j in range(i+1, len(objects)):
            if objects[j].position.x < objects[mini].position.x :
                mini = j
        objects[i] , objects[mini]  = objects[mini] , objects[i]
    return objects
        
def is_colliding(obj1, obj2):
    if (obj1.position.y < obj2.position.y + obj2.height and obj1.position.y + obj1.height > obj2.position.y):
        return [obj1, obj2]

def find_possiblcol(objectlist):
    possible_col = []
    for i in range(len(objectlist) - 1):
        if (objectlist[i].position.x < objectlist[i+1].position.x + objectlist[i+1].width and
        objectlist[i].position.x + objectlist[i].width > objectlist[i+1].position.x ):
            possible_col.append((objectlist[i], objectlist[i+1]))
    return possible_col

def check_collitions(objectlist):
    sorted = tri_selection(objectlist)
    pos_col = find_possiblcol(sorted)

    for i in range(len(pos_col)):

  
        if is_colliding(pos_col[i][0], pos_col[i][1]):

            if isinstance(pos_col[i][0], FlyGobelin) and isinstance(pos_col[i][1], FireBall):
                pos_col[i][0].hide = True
                pos_col[i][1].hide = True
                pygame.mixer.music.load(SOUNDS["Explosion"])
                pygame.mixer.music.play(1)
            if isinstance(pos_col[i][0], FireBall) and isinstance(pos_col[i][1], FireBall):
                pos_col[i][0].hide = True
                pos_col[i][1].hide = True
                pygame.mixer.music.load(SOUNDS["Explosion"])
                pygame.mixer.music.play(1)