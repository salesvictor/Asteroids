import pygame as pg
from random import randint

from models.Saucer import Saucer
from models.Bullet import Bullet


class BigSaucer(Saucer):

    def __init__(self, screen, x=None, y=None, speed=None, vel_dir=None):
        self.bullet_timer = 0
        super().__init__(screen, 0.6, x, y, speed, vel_dir)

    def shoot(self):
        self.direction = randint(0, 360)
        bullet = Bullet(self.screen, self.x, self.y, self.direction)
        self.saucer_shot_bullets.add(bullet)

    def update(self):
        self.bullet_timer = (self.bullet_timer + 1) % 100
        if self.bullet_timer == 50:
            self.shoot()
        
        super().update()
