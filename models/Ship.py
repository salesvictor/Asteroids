import pygame as pg
from math import cos, sin, radians
from models.GameObject import GameObject
from models.Bullet import Bullet


class Ship(GameObject):
    ACCEL = 0.2
    DEACCEL = 0.09
    MAX_SPEED = 4.5
    SHOT_DELAY = 5
    TURN_SPEED = -5

    def __init__(self, screen, x, y):
        super().__init__(x, y, 0, (0, 0), 0, screen, 'ship.png', 0.1)
        self.shot_bullets = []
        self.bullets_sprite = pg.sprite.Group()

    def update(self):
        self.speed = max(self.speed - self.DEACCEL, 0)

        self.bullets_sprite.update()
        super().update()

    def turn(self, angle):
        self.image = pg.transform.rotate(self.original_image, self.direction + angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.direction += angle

    def shoot(self):
        if not self.shot_bullets or self.shot_bullets[-1].age > self.SHOT_DELAY:
            bullet = Bullet(self.screen, self.x, self.y, -self.direction)
            self.shot_bullets.append(bullet)
            self.bullets_sprite.add(bullet)

    def destroy(self):
        # TODO(Victor) write destroy
        pass
