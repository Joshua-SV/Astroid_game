from circleshape import *
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    contianers = None

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # check if this is a small circle
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            angle = random.uniform(20,50) # get a random degree angle for new asteriods
            # create two new vector pointing orthogonally from the velocity vector
            new_vector1 = self.velocity.rotate(angle)
            new_vector2 = self.velocity.rotate(-angle)
            # new radius of split asteriod
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # create two new asteriods
            x, y = self.position
            split1 = Asteroid(x, y, new_radius)
            split2 = Asteroid(x, y, new_radius)
            split1.velocity = new_vector1 * 1.2
            split2.velocity = new_vector2 * 1.2
            self.kill()

        