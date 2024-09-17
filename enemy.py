from vector import Vector2
from storage import *

class FlyGobelin:
    def __init__(self, position):
        self.position = position
        self.attackdist = 500
        self.dirrection = Vector2(0, 0)
        self.anim_frame = 0
        self.speed = 1
        self.sprite = ANIMATION_SPRITES["gobelin"][self.anim_frame]
      
    def move(self, playerpos):
        dist = playerpos.distance([self.position.x, self.position.y])
        print(dist.x + dist.y)
        if dist.x + dist.y > self.attackdist or  dist.x + dist.y < -self.attackdist:  
            dist.normalise()
            dist.pluse(dist.normalise()*Vector2(self.speed, self.speed))
            self.position.pluse(Vector2(dist.x, dist.y if dist.y > 100 ))
        else:
            self.attack()
    
    def attack(self):
        pass
    
    def get_sprite(self):
        return self.sprite
    
    def get_pos(self):
        return self.position.x, self.position.y