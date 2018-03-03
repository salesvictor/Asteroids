import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pygame
from models.Ship import Ship
from models.BigAsteroid import BigAsteroid
from models.MediumAsteroid import MediumAsteroid
from models.SmallAsteroid import SmallAsteroid
from models.Saucer import Saucer


if __name__ == '__main__':
    pygame.init()  # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((800, 640))

    # Crating a saucer object and list as sprite
    ship = Ship(main_surface, 20, 20)
    big_asteroid = BigAsteroid(60, 40, main_surface)
    medium_asteroid = MediumAsteroid(60, 160, main_surface)
    small_asteroid = SmallAsteroid(60, 240, main_surface)
    saucer = Saucer(200, 30, main_surface)

    ships_group = pygame.sprite.Group()
    big_asteroids_group = pygame.sprite.Group()
    medium_asteroids_group = pygame.sprite.Group()
    small_asteroids_group = pygame.sprite.Group()
    saucers_group = pygame.sprite.Group()

    ships_group.add(ship)
    big_asteroids_group.add(big_asteroid)
    medium_asteroids_group.add(medium_asteroid)
    small_asteroids_group.add(small_asteroid)
    saucers_group.add(saucer)

    while True:
        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break  # Leave game loop

        main_surface.fill((0, 0, 0))
        ships_group.draw(main_surface)
        big_asteroids_group.draw(main_surface)
        medium_asteroids_group.draw(main_surface)
        small_asteroids_group.draw(main_surface)
        saucers_group.draw(main_surface)

        # Now that everything is drawn, put it on display!
        pygame.display.flip()

    pygame.quit()
