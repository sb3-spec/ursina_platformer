from ursina import Sprite, held_keys

class Character(Sprite):
    def __init__(self):
        super().__init__()
        
        # horizontal velocity
        self.dx = 0
        # vertical velocity
        self.dy = 0
        # friction value
        self.friction = .05
        # players accel
        self.accel = .3
        self.is_running = False
        self.running_mult = 1.2
        
    def update(self):
        # checking 
        going_right = held_keys['right arrow'] or held_keys['d']
        going_left = held_keys['left arrow'] or held_keys['a']    
        
        if going_right:
            if self.dx > 0:
                self.dx += self.accel - self.friction
            elif self.dx < 0:
                self.dx += self.accel + self.friction
        
        if going_left:
            if self.dx > 0:
                self.dx -= self.accel - self.friction
            elif self.dx < 0:
                self.dx -= self.accel + self.friction
            
        if self.dx and not going_left:
            # if moving to right
            if self.dx > 0:
                self.dx -= self.friction
            elif self.dx < 0:
                self.dx += self.friction
                
        
                
        