from storage import *

class Player:
    def __init__(self, position, time):
        self.velocity = Vector2(0, 0)
        self.position = position
        self.onground = True
        self.moving = False
        self.anim_frame = 0
        self.animation = "Idle"
        self.sprite = ANIMATION_SPRITES[self.animation][self.anim_frame]
        self.dirrection = "right"
        self.animation_speed = .15
        self.timestore = time
        
    def set_dirrection(self, dire):
        self.dirrection = dire
    
    def get_pos(self):
        return self.position.x ,  self.position.y

    def get_sprite(self):
        return self.sprite 
        
    def add_velocity(self, vector):
        self.velocity += vector
        
    def is_onground(self):
        if GRAVITY.y > 0:
            if self.position.y < GROUND:
                self.onground = False
            else :
                self.onground = True
                self.velocity.y = 0
        else:
            if self.position.y > CELLING:
                self.onground = False
            else :
                self.onground = True
                self.velocity.y = 0
        return self.onground
            
    def is_moving(self, status):
        self.moving = status
            
    def set_animation(self, anim = None):
        if anim == None:    
            if not self.moving:
                self.animation = "Idle"
            else:
                self.animation = "Run"
            if not self.onground:
                self.animation = "Fall"
        else:
            self.animation = anim

        
    def animation_run(self):
        if self.anim_frame >= len(ANIMATION_SPRITES[self.animation]):
            self.anim_frame = 0
        print(self.anim_frame)
        
        self.sprite = pygame.transform.flip(ANIMATION_SPRITES[self.animation][self.anim_frame], False, False if GRAVITY.y > 0 else True) if self.dirrection == "right" else pygame.transform.flip(ANIMATION_SPRITES[self.animation][self.anim_frame], True, False if GRAVITY.y > 0 else True)
        self.anim_frame += 1
        
    def update(self, time):
        if self.timestore + self.animation_speed < time:
            self.timestore = time
            self.animation_run()
        self.velocity_on_pos()
        self.is_onground()
        self.app_friction()
        self.app_gravity()
        self.set_animation()
        
    def velocity_on_pos(self):
        self.position += self.velocity
        if self.velocity.x > (GROUND_FRICTION * Vector2(2, 2)).x:
            self.velocity.x = (GROUND_FRICTION * Vector2(2, 2)).x
 
        if self.velocity.x < -(GROUND_FRICTION * Vector2(2, 2)).x:
            self.velocity.x = -(GROUND_FRICTION * Vector2(2, 2)).x

    
    def app_friction(self):
        
        self.velocity.x *= GROUND_FRICTION.x
        self.velocity.y *= AIR_FRICTION.x

    def app_gravity(self):
        if self.onground == False:
            self.velocity.y += GRAVITY.y