import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pygame
from math import cos, sin, radians, log
from random import randint, lognormvariate, uniform
from models.GameObject import GameObject


class Asteroid(GameObject):
    SPEED_MU = 0
    SPEED_SIGMA = (2 * log(2)) ** 0.5

    def __init__(self, screen, img_factor):
        """
        Description
        """
        self.ANGLE_SPEED = uniform(0, 2)
        # Generate a random position on the border for the asteroid to be
        # created
        x = 0
        y = 0
        (width, height) = screen.get_size()

        i = randint(1, 4)
        if i == 1:  # Left border
            y = randint(1, 639)
        elif i == 2:  # Top border
            x = randint(1, 799)
        elif i == 3:  # Right border
            x = width
            y = randint(1, 639)
        else:  # Bottom border
            x = randint(1, 799)
            y = height

        # Generate velocity direction and speed
        speed = lognormvariate(self.SPEED_MU, self.SPEED_SIGMA)
        angle = radians(uniform(0, 360))
        vel_dir = (cos(angle), sin(angle))

        super().__init__(x, y, 0, vel_dir, speed, screen,
                         'asteroid.png', img_factor)

    def update(self):
        super().update()

        self.direction += self.ANGLE_SPEED
        self.image = pygame.transform.rotate(self.original_image, self.direction)
        self.rect = self.image.get_rect(center=(self.x, self.y))