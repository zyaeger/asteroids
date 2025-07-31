import sys

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from score import Score
from sprites.asteroid import Asteroid
from sprites.asteroidfield import AsteroidField
from sprites.player import Player
from sprites.shot import Shot


def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable

    # pylint: disable=unused-variable
    field = AsteroidField()
    score = Score()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, drawable, updatable)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                sys.exit(0)

            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    shot.kill()
                    score.score_up()

        screen.fill("black")
        score.show_score(screen)

        for shape in drawable:
            shape.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0  # seconds


if __name__ == "__main__":
    main()
