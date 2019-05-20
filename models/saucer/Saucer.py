import pygame as pg
import os
from math import cos, sin, radians, log
from random import randint, uniform

from models.GameObject import GameObject
from assets.sfx.Sounds import Sounds


class Saucer(GameObject):
    SPEED_MU = log(4/3)
    SPEED_SIGMA = 0.8

    def __init__(self, screen, img_file, img_factor, x=None, y=None, speed=None,
                 vel_dir=None):
        """
        Description
        """
        if x is None and y is None:
            # Generate a random position on the border for the saucer to be
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
        if vel_dir is None:
            vel_dir = (cos(angle), sin(angle))
        if speed is None:
            speed = [3*vel_dir[0], 3*vel_dir[1]]

        super().__init__(x, y, 0, speed, screen, img_file, img_factor)

        self.saucer_shot_bullets = pg.sprite.Group()

    def update(self):
        self.saucer_shot_bullets.update()

        super().update()

    def kill(self):
        for bullet in self.saucer_shot_bullets:
            bullet.kill()
        super().kill()

        Sounds.big_explosion_sound()
