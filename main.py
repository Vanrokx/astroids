# this allows us to use code
# the open-source pygame library
# throughout this fiele
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_background = pygame.Color(0,0,0)
    while True:
        pygame.Surface.fill(screen, screen_background)
        #quit the game if the user clicks the X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        
        
        
        
        pygame.display.flip()
    # print("Starting asteroids!")
    # print("Screen width:",SCREEN_WIDTH)
    # print("Screen height:",SCREEN_HEIGHT)

if __name__ == "__main__":
    main()