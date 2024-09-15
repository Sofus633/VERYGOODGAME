import math

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def pluse(self, voct):
        self.x = self.x + voct.x
        self.y = self.y + voct.y

    
    def __mul__(self, scalar):
        
        return Vector2(self.x * scalar.x, self.y * scalar.y)
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def get_vect(self):
        return self.x , self.y
    
    def set(self, tup):
        self.x , self.y = tup[0], tup[1]
        
    def normalise(self):
        mangitude = self.magnitude()
        self.x /= mangitude
        self.y /= mangitude
        return self