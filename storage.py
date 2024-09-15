import pygame
import os
from vector import Vector2
from logic import *
import math
import random
ANIMATION_SPRITES = {}
GROUND_FRICTION = Vector2(0.20, 0.20)
AIR_FRICTION = Vector2(0.95, 0.95)
GRAVITY = Vector2(0, .2)
GROUND = 700
CELLING = 100

ANIM_INFO = {
    "jump" : 1,
    "fireball" : .1
}
SOUNDS = {
    "Fireball" : "sounds/Fireball.mp3",
}



def init_sprites():
    
    SPRITE_HEIGHT = 86
    SPRITE_WIGHT = 60
    sprites = []
    ls_d = os.listdir("Wizard")
    for i in range(len(ls_d)):
        sprites.append([])
        sprite_sheet = pygame.image.load("Wizard/" + ls_d[i]).convert_alpha()
        sprite_wight = math.ceil(sprite_sheet.get_size()[0] / int(ls_d[i][0]))


        sprite_height = sprite_sheet.get_size()[1]
        sheet_width, sheet_height = sprite_sheet.get_size()
        for x in range(sheet_width//sprite_wight):
                left = x * sprite_wight
                top = 0
                rect = pygame.Rect(left, top, sprite_wight, sprite_height)
                sprite = sprite_sheet.subsurface(rect)
                sprites[-1].append(sprite)
                if sheet_width % sprite_wight != 0 and x == (sheet_width//sprite_wight) - 1:
                    remaining_width = sheet_width % sprite_wight
                    rect = pygame.Rect(sheet_width - remaining_width, 0, remaining_width, sprite_height)
                    sprite = sprite_sheet.subsurface(rect)
                    sprites[-1].append(sprite)
                    
        ANIMATION_SPRITES[''.join([char for char in ls_d[i].replace(".png", "") if not char.isdigit()])] = sprites[-1]
        #display_dict(ANIMATION_SPRITES)

                                             
        
        
