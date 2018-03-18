from math import sin, cos, radians
from models.GameObject import GameObject


class Bullet(GameObject):
    LIFE_TIME = 50  # Max of cycles the bullet can exist

    def __init__(self, screen,  x, y, direction):
        super().__init__(x, y, direction, (cos(radians(direction)), sin(radians(direction))),
                         10, screen, 'bullet.png', 0.75)

        self.age = 0  # Number of cycles since the bullet was cast

    def update(self):
        self.x += self.speed * self.vel_dir[0]
        self.y += self.speed * self.vel_dir[1]
        self.rect.center = (self.x, self.y)
        self.direction = (self.direction + 360) % 360

        self.check_on_border()

        self.age += 1
        if self.age > self.LIFE_TIME:
            self.kill()

    def kill(self):
        super().kill()
        # TODO(Victor) write kill
