import pygame as pg
from math import atan, degrees, pi

from models.Saucer import Saucer
from models.Bullet import Bullet


class SmallSaucer(Saucer):

    def __init__(self, screen, player, x=None, y=None, speed=None,
                 vel_dir=None):
        self.bullet_timer = 0
        super().__init__(screen, 'small_saucer.png', 1.2, x, y, speed, vel_dir)
        self.player = player

    def shoot(self):
        dy = -(self.player.y - self.y)
        dx = self.player.x - self.x

        if dx > 0 and dy > 0:
            self.direction = atan(dy/dx)
        elif dx < 0 and dy < 0:
            self.direction = pi + atan(dy/dx)
        elif dx > 0 and dy < 0:
            self.direction = atan(dy/dx)
        else:
            self.direction = pi + atan(dy/dx)
        self.direction = degrees(self.direction)
        bullet = Bullet(self.screen, self.x, self.y, -self.direction)
        self.saucer_shot_bullets.add(bullet)

    def update(self):
        self.bullet_timer = (self.bullet_timer + 1) % 200
        if self.bullet_timer == 100:
            self.shoot()

        super().update()
