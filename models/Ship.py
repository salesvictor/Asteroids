import pygame as pg
from math import cos, sin, radians
from models.GameObject import GameObject
from models.Bullet import Bullet


class Ship(GameObject):
    ACCEL = 0.2
    DEACCEL = 0.09
    MAX_SPEED = 4.5
    SHOT_DELAY = 5
    TURN_SPEED = 5

    def __init__(self, screen, x, y):
        super().__init__(x, y, 0, (0, 0), 0, screen, 'ship.png', 0.1)
        self.shot_bullets = []

    def update(self):
        self.speed = max(self.speed - self.DEACCEL, 0)

        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.speed = min(self.speed + self.ACCEL, self.MAX_SPEED)
            self.vel_dir = (cos(radians(self.direction)), sin(radians(self.direction)))
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.turn(self.TURN_SPEED)
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.turn(-self.TURN_SPEED)

        super().update()

    def turn(self, angle):
        self.image = pg.transform.rotate(self.original_image, self.direction + angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.direction += angle

    def shoot(self):
        if not self.shot_bullets or self.shot_bullets[-1].age > self.SHOT_DELAY:
            bullet = Bullet(self.screen, self.x, self.y, -self.direction)
            self.shot_bullets.append(bullet)

    def destroy(self):
        # TODO(Victor) write destroy
        pass
