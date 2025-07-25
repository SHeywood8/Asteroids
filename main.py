import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        pygame.Surface.fill(screen, color=(0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        time = clock.tick(60)
        dt = time / 1000


if __name__ == "__main__":
    main()
