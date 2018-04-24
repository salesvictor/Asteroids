from math import atan, degrees, pi, sqrt
from random import randint

from models.Saucer import Saucer
from models.Bullet import Bullet
from assets.sfx.SmallSaucerSound import SmallSaucerSound


class SmallSaucer(Saucer):
    MAX_SHOOTING_ANGLE = 10
    ANGLE_RANGE = 10

    def __init__(self, screen, round, player, x=None, y=None, speed=None,
                 vel_dir=None):
        self.bullet_timer = 0
        super().__init__(screen, 'small_saucer.png', 1.2, x, y, speed, vel_dir)
        self.round = round
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

        angle_factor = randint(-self.ANGLE_RANGE, self.ANGLE_RANGE)
        angle_factor = angle_factor/self.ANGLE_RANGE
        rand_angle = 1/sqrt(float(self.round)) * angle_factor * self.MAX_SHOOTING_ANGLE

        bullet = Bullet(self.screen, self.x, self.y, -(self.direction+rand_angle))
        self.saucer_shot_bullets.add(bullet)

    def update(self):
        self.bullet_timer = (self.bullet_timer + 1) % 100
        if self.bullet_timer == 75:
            self.shoot()

        super().update()

        SmallSaucerSound()
