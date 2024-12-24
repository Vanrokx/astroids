# this allows us to use code
# the open-source pygame library
# throughout this fiele
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_background = pygame.Color(0,0,0)

    #Clock
    clock = pygame.time.Clock()
    dt = 0

    #player init
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Game Loop
    while True:
        pygame.Surface.fill(screen, screen_background)
        #quit the game if the user clicks the X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.draw(screen)
        
        
        
        time_passed = clock.tick(60)
        dt = time_passed / 1000
        pygame.display.flip()
    # print("Starting asteroids!")
    # print("Screen width:",SCREEN_WIDTH)
    # print("Screen height:",SCREEN_HEIGHT)

if __name__ == "__main__":
    main()