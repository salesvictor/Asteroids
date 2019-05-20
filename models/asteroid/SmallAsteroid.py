from math import sqrt

from models.asteroid.Asteroid import Asteroid
from assets.sfx.Sounds import Sounds


class SmallAsteroid(Asteroid):
    SMALL_ASTEROID_MAX_SPEED = 3.0

    def __init__(self, screen, x=None, y=None, speed=None, vel_dir=None):
        super().__init__(screen, 'small_asteroid.png', 1.0, x, y, speed, vel_dir)
        speed_module = sqrt(self.speed[0] ** 2 + self.speed[1] ** 2)
        new_speed_module = min(speed_module, self.SMALL_ASTEROID_MAX_SPEED)
        self.speed = [self.speed[0] * new_speed_module/speed_module, self.speed[1] * new_speed_module/speed_module]

    def kill(self):
        super().kill()

        Sounds.small_explosion_sound()