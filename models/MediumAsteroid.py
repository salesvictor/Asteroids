from random import gauss
from math import cos, sin, radians
from models.Asteroid import Asteroid
from models.SmallAsteroid import SmallAsteroid


class MediumAsteroid(Asteroid):

    def __init__(self, screen, x=None, y=None, speed=None, vel_dir=None):
        super().__init__(screen, 'medium_asteroid.png', 0.5, x, y, speed, vel_dir)

    def kill(self):
        groups = self.groups()  # Store the groups on which the asteroid was
        super().kill()  # Exclude the asteroid form the groups

        spread_angle = gauss(0, 45)
        spread_speed = gauss(0, 1)

        vel_dir1 = (cos(radians(self.direction + spread_angle)),
                    sin(radians(self.direction + spread_angle)))
        vel_dir2 = (cos(radians(self.direction - spread_angle)),
                    sin(radians(self.direction - spread_angle)))
        speed1 = self.speed + spread_speed
        speed2 = self.speed - spread_speed

        # Add two smaller asteroids to the groups
        for group in groups:
            group.add([SmallAsteroid(self.screen, self.x, self.y,
                                     speed1, vel_dir1),
                       SmallAsteroid(self.screen, self.x, self.y,
                                     speed2, vel_dir2)])
