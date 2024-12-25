import pygame

# base class for game objects inherets from pygame
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # place each class sprite in a group specified by you
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides(self, TargetCircle):
        # check distance between two cricles
        distance = self.position.distance_to(TargetCircle.position)
        # chech if both circles are colliding by checking the distance vs radius of both circles
        if distance <= (self.radius + TargetCircle.radius):
            return True
        
        return False
