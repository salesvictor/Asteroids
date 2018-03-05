import os
import sys
from math import sin, cos, radians

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pygame
from models.GameObject import GameObject


class Bullet(GameObject):
    def __init__(self, screen,  x, y, direction):
        super().__init__(x, y, direction, (cos(radians(direction)), sin(radians(direction))), 10, screen, 'bullet.png', 0.5)
        self.life_time = 40
        self.age = 0

    def update(self):
        self.age += 1

        if self.age > self.life_time:
            self.destroy()

        else:
            self.x += self.speed * self.vel_dir[0]
            self.y += self.speed * self.vel_dir[1]
            self.rect = self.image.get_rect(center=(self.x, self.y))

        self.check_on_border()

    def destroy(self):
        self.kill()