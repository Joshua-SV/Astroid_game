# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init() # initialize the pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")  # Optional: Set a window title
    clock = pygame.time.Clock() # create an object for FPS 
    dt = 0
    # create groups for game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets_active = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, bullets_active)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # create player object
    asteroidsfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        # using groups to manage all objects
        for obj in updatable:
            obj.update(dt) # makes the player and others rotate and move

        for obj in asteroids:
            if obj.collides(player): # check if asteriod collided with player
                print("GAME OVER!!!")
                exit(0) # end game

        for item in drawable:
            item.draw(screen) # draw player and others on screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # ensures a 60 FPS 

if __name__ == "__main__":
    main()