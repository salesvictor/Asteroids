import pygame as pg
from math import sin, cos, radians

from models.GameObject import GameObject
from assets.sfx.Sounds import Sounds


class Bullet(GameObject):
    LIFE_TIME = 50  # Max of cycles the bullet can exist
    SPEED_MODULE = 10

    def __init__(self, screen,  x, y, direction):
        super().__init__(x, y, direction, [self.SPEED_MODULE*cos(radians(direction)),
                         self.SPEED_MODULE*sin(radians(direction))], screen, 'bullet.png', 0.6)

        self.age = 0  # Number of cycles since the bullet was cast

        Sounds.shoot_sound()

    def update(self):
        self.age += 1
        if self.age > self.LIFE_TIME:
            self.kill()

        super().update()

        last_pos = [self.mask_surface.get_rect().center[0] - int(self.speed[0]),
                    self.mask_surface.get_rect().center[1] - int(self.speed[1])]
        # Drawing the bullets trajectory to mask surface to prevent from tunneling
        pg.draw.line(self.mask_surface, (200, 150, 150), last_pos, self.mask_surface.get_rect().center, 5)
        self.mask = pg.mask.from_surface(self.mask_surface)

    def kill(self):
        super().kill()
