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
        spread_speed = gauss(0, 0.5)

        vel_dir1 = (cos(radians(self.direction + spread_angle)),
                    sin(radians(self.direction + spread_angle)))
        vel_dir2 = (cos(radians(self.direction - spread_angle)),
                    sin(radians(self.direction - spread_angle)))
        speed1 = []
        speed1.append(self.speed[0] + spread_speed * vel_dir1[0])
        speed1.append(self.speed[1] + spread_speed * vel_dir1[1])

        speed2 = []
        speed2.append(self.speed[0] - spread_speed * vel_dir2[0])
        speed2.append(self.speed[1] - spread_speed * vel_dir2[1])

        # Add two smaller asteroids to the groups
        for group in groups:
            group.add([SmallAsteroid(self.screen, self.x, self.y,
                                     speed1, vel_dir1),
                       SmallAsteroid(self.screen, self.x, self.y,
                                     speed2, vel_dir2)])
