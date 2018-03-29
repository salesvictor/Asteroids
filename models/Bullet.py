from math import sin, cos, radians
from models.GameObject import GameObject


class Bullet(GameObject):
    LIFE_TIME = 50  # Max of cycles the bullet can exist
    SPEED_MODULE = 10

    def __init__(self, screen,  x, y, direction):
        super().__init__(x, y, direction, [self.SPEED_MODULE*cos(radians(direction)),
                         self.SPEED_MODULE*sin(radians(direction))], screen, 'bullet.png', 0.75)

        self.age = 0  # Number of cycles since the bullet was cast

    def update(self):
        self.age += 1
        if self.age > self.LIFE_TIME:
            self.kill()

        super().update()

    def kill(self):
        super().kill()
        # TODO(Victor) write kill
