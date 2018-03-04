import pygame as pg
from math import cos, sin, radians, log
from random import randint, lognormvariate, uniform
from models.GameObject import GameObject


class Asteroid(GameObject):
    SPEED_MU = log(4/3)
    SPEED_SIGMA = 0.8

    def __init__(self, screen, img_factor, x=None, y=None, speed=None, vel_dir=None):
        """
        Description
        """
        self.ANGLE_SPEED = uniform(0, 2)

        if x is None and y is None:
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

        angle = radians(uniform(0, 360))
        if speed is None:
            speed = lognormvariate(self.SPEED_MU, self.SPEED_SIGMA)
        if vel_dir is None:
            vel_dir = (cos(angle), sin(angle))

        super().__init__(x, y, 0, vel_dir, speed, screen,
                         'asteroid.png', img_factor)

    def update(self):
        super().update()

        self.direction += self.ANGLE_SPEED
        self.image = pg.transform.rotate(self.original_image, self.direction)
        self.rect = self.image.get_rect(center=(self.x, self.y))