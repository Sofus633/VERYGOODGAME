
from player import Player
from fireball import FireBall
from vector import Vector2
from logic import *
from storage import *
from tilemap import TileMap
from enemy import FlyGobelin
pygame.init()
pygame.display.set_caption('VERRYGOODGAME')
pygame.mixer.music.set_volume(.5)
init_sprites()


running = True

def initplayer():
    """ will allow chosing player skin / weapon maybe """
    plr = Player(SPAWN_POSITION_PL, time.time())
    return plr

def displayplayer():
    screen.blit(player1.get_sprite(), player1.get_pos())


def displayfireball(fireball):
    screen.blit(fireball.get_sprite(), fireball.get_pos())

def displayfireballs():
    for fireball in allfireballs:
        displayfireball(fireball)
        fireball.move(pygame.mouse.get_pos(), player1.get_pos())
        if fireball.position.get_vect()[0] > screen.get_size()[0] or fireball.position.get_vect()[0] < 0 or fireball.position.get_vect()[1] < 0 or fireball.position.get_vect()[1] > screen.get_size()[1]:
            allfireballs.remove(fireball)
    
def displaygobelin():
    screen.blit(goblein.get_sprite(), goblein.get_pos())

    
    
def display_all():
    tilemap.display()
    displayfireballs()
    displayplayer()
    displaygobelin()

player1 = initplayer()
goblein = FlyGobelin(Vector2(100, 199))
tilemap = TileMap(MAP, screen, "Tiles/Basic.png")
while running:
    timee = time.time()
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

    if keys[pygame.K_x]:
        print("cast fireball 1",timee, fireball_clock )
        if fireball_clock + .1 < timee and player1.is_onground():
            print("cast fireball 2")
            fireball_clock = timee
            player1.casting_fireball = True
            cast_fireball_clock = timee
            fireball_clock = timee
            player1.animation_speed = ANIM_INFO["fireball"]
            player1.anim_frame = 0

    if keys[pygame.K_e]:
        GRAVITY.y  -= .01
        print(GRAVITY.y)
        
    if keys[pygame.K_a]:
        GRAVITY.y  += .01
        print(GRAVITY.y)
        
    if keys[pygame.K_z]:
        if player1.is_onground() and GRAVITY.y > 0:
            player1.add_velocity(Vector2(0, -speed * 3))
    elif keys[pygame.K_s]:
        if player1.is_onground() and GRAVITY.y < 0:
            player1.add_velocity(Vector2(0, speed* 3))
        
    if keys[pygame.K_q]:
        player1.set_dirrection("left")
        player1.add_velocity(Vector2(-speed, 0))
        player1.is_moving(True)
    elif keys[pygame.K_d]:
        player1.set_dirrection("right")
        player1.add_velocity(Vector2(speed, 0))
        player1.is_moving(True)
    else:
        player1.is_moving(False)
        
    if not (keys[pygame.K_z] or keys[pygame.K_s] or keys[pygame.K_q] or keys[pygame.K_d]):
        if event.type == pygame.QUIT:
            running = False
            
    
    if  player1.cast == True:
        player1.cast = False
        player1.casting_fireball    = False
        casting_fireball = timee
        playerpos = player1.get_pos()
        player1.animation_speed = .15
        
        if len(allfireballs) > 0 :
            allfireballs[-1].controlled = False
            
        allfireballs.append(FireBall(playerpos[0] + 95, playerpos[1] +20))
        
    display_all()
    player1.update(time.time())
    goblein.move(player1.position)
    
    pygame.display.flip()
    screen.fill(0)
    clock.tick(60) 