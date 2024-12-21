# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init() # initialize the pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")  # Optional: Set a window title
    clock = pygame.time.Clock() # create an object for FPS 
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,255,255))
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # ensures a 60 FPS 

if __name__ == "__main__":
    main()