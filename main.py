import pygame
from player import Player
from vector import Vector2
from logic import *
from storage import *
import time

pygame.init()
screen = pygame.display.set_mode((1920//2, 1080//2))
pygame.display.set_caption('VERRYGOODGAME')

init_sprites()

SPAWN_POSITION_PL = Vector2(100, 100)
clock = pygame.time.Clock() 
running = True

def initplayer():
    """ will allow chosing player skin / weapon maybe """
    plr = Player(SPAWN_POSITION_PL, time.time())
    return plr

def displayplayer():
    screen.blit(player1.get_sprite(), player1.get_pos())
    #print(f"displayed at {player1.get_pos()}")


player1 = initplayer()
speed = 3

while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        if player1.is_onground():
            player1.add_velocity(Vector2(0, -speed * 3))
    elif keys[pygame.K_s]:
        player1.add_velocity(Vector2(0, speed))

    if keys[pygame.K_q]:
        player1.add_velocity(Vector2(-speed, 0))
        player1.set_dirrection("left")
        player1.is_moving(True)
    elif keys[pygame.K_d]:
        player1.is_moving(True)
        player1.set_dirrection("right")
        player1.add_velocity(Vector2(speed, 0))
    else:
        player1.is_moving(False)
    if not (keys[pygame.K_z] or keys[pygame.K_s] or keys[pygame.K_q] or keys[pygame.K_d]):
        if event.type == pygame.QUIT:
            running = False
    displayplayer()
    player1.update(time.time())
    
    pygame.display.flip()
    screen.fill(0)
    clock.tick(60) 