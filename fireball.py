from vector import *
from storage import *


class FireBall:
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.dirrection = Vector2(1, 0)
        self.anim_frame = 0
        self.controlled = True
        self.sprite = ANIMATION_SPRITES["Fireball"][self.anim_frame]
        
    def move(self, mousepos, playerpos):
        if self.controlled:
            self.dirrection = Vector2(mousepos[0] - playerpos[0], mousepos[1] - playerpos[1]).normalise() * Vector2(7, 7)
        self.position += self.dirrection
            
        print(self.dirrection.get_vect())

    def update(self):
        self.move()
    
    def get_sprite(self):
        return self.sprite
    
    def get_pos(self):
        return self.position.x ,  self.position.y
