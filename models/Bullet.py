from math import sin, cos, radians
from models.GameObject import GameObject


class Bullet(GameObject):
    LIFE_TIME = 40

    def __init__(self, screen,  x, y, direction):
        super().__init__(x, y, direction, (cos(radians(direction)), sin(radians(direction))),
                         10, screen, 'bullet.png', 0.5)
        self.age = 0

    def update(self):
        super().update()

        self.age += 1
        if self.age > self.LIFE_TIME:
            self.destroy()

    def destroy(self):
        self.kill()
