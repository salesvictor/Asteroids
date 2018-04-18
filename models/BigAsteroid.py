from random import gauss
from math import cos, sin, radians, sqrt

from models.Asteroid import Asteroid
from models.MediumAsteroid import MediumAsteroid
from assets.sfx.BigExplosionSound import BigExplosionSound


class BigAsteroid(Asteroid):
    BIG_ASTEROID_MAX_SPEED = 2.0

    def __init__(self, screen, x=None, y=None, speed=None, vel_dir=None):
        super().__init__(screen, 'big_asteroid.png', 0.4, x, y, speed, vel_dir)
        speed_module = sqrt(self.speed[0] ** 2 + self.speed[1] ** 2)
        new_speed_module = min(speed_module, self.BIG_ASTEROID_MAX_SPEED)
        self.speed = [self.speed[0] * new_speed_module / speed_module, self.speed[1] * new_speed_module / speed_module]

    def kill(self):
        groups = self.groups()  # Store the groups on which the asteroid was
        super().kill()  # Exclude the asteroid from the groups

        BigExplosionSound()

        spread_angle = gauss(0, 45)
        spread_speed = gauss(0, 1)

        vel_dir1 = (cos(radians(self.direction+spread_angle)),
                    sin(radians(self.direction+spread_angle)))
        vel_dir2 = (cos(radians(self.direction-spread_angle)),
                    sin(radians(self.direction-spread_angle)))

        speed1 = []
        speed1.append(self.speed[0] + spread_speed*vel_dir1[0])
        speed1.append(self.speed[1] + spread_speed*vel_dir1[1])

        speed2 = []
        speed2.append(self.speed[0] - spread_speed*vel_dir2[0])
        speed2.append(self.speed[1] - spread_speed*vel_dir2[1])

        # Add two smaller asteroids to the groups
        new_asteroids = [MediumAsteroid(self.screen, self.x, self.y, speed1,
                                        vel_dir1),
                         MediumAsteroid(self.screen, self.x, self.y, speed2,
                                        vel_dir2)]
        for group in groups:
            group.add(new_asteroids)
