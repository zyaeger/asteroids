import pygame

from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting Asteroids!")
                return
            
        updatable.update(dt)

        screen.fill("black")

        for shape in drawable:
            shape.draw(screen)
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0  # seconds


if __name__ == "__main__":
    main()
