import pygame as pg
from math import cos, sin, radians
from models.GameObject import GameObject
from models.Bullet import Bullet


class Ship(GameObject):
    ACCEL = 0.2
    DEACCEL = 0.005
    MAX_SPEED = 3
    SHOT_DELAY = 5
    TURN_SPEED = -2

    def __init__(self, screen, x, y):
        super().__init__(x, y, 0, (0, 0), 0, screen, 'ship.png', 0.1)
        self.shot_bullets = pg.sprite.Group()

    def update(self):
        self.speed = max(self.speed - self.DEACCEL, 0)

        self.shot_bullets.update()
        super().update()

    def turn(self, angle):
        self.image = pg.transform.rotate(self.original_image, self.direction + angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.direction += angle

    def check_bullets_collision(self, sprites_group):
        pg.sprite.groupcollide(self.shot_bullets, sprites_group, True, True, pg.sprite.collide_mask)

    def shoot(self):
        if len(self.shot_bullets) == 0 or self.shot_bullets.sprites()[-1].age > self.SHOT_DELAY:
            bullet = Bullet(self.screen, self.x, self.y, -self.direction)
            self.shot_bullets.add(bullet)

    def kill(self):
        super().kill()
        # TODO(Victor) write kill
