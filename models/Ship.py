import pygame as pg
from math import cos, sin, radians
from models.GameObject import GameObject
from models.Bullet import Bullet


class Ship(GameObject):
    #  Movement constants
    ACCEL = 0.2
    DEACCEL = 0.01
    MAX_SPEED = 3
    SHOT_DELAY = 10
    MAX_SHOT_BULLETS = 4
    RECHARGE_BULLETS_TIME = 70
    TURN_SPEED = -2

    def __init__(self, screen, x, y):
        super().__init__(x, y, 0, (0, 0), 0, screen, 'ship.png', 0.1)
        self.shot_bullets = pg.sprite.Group()
        self.time_since_discharge = self.RECHARGE_BULLETS_TIME

    #  Update the ship and its bullets movement
    def update(self):
        self.speed = max(self.speed - self.DEACCEL, 0)

        self.shot_bullets.update()

        self.time_since_discharge += 1

        super().update()

    #  Rotate the ship
    def turn(self, angle):
        self.image = pg.transform.rotate(self.original_image, self.direction + angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.direction += angle

    #  Check for its bullets collisions and kill the objects colliding
    def check_bullets_collision(self, sprites_group):
        pg.sprite.groupcollide(self.shot_bullets, sprites_group, True, True, pg.sprite.collide_mask)

    #  Cast a bullet in the direction the ship is pointing
    def shoot(self):
        print(len(self.shot_bullets.sprites()))
        if self.time_since_discharge > self.RECHARGE_BULLETS_TIME:
            if len(self.shot_bullets.sprites()) == 0 or \
                (len(self.shot_bullets.sprites()) < self.MAX_SHOT_BULLETS and
                self.shot_bullets.sprites()[-1].age > self.SHOT_DELAY):

                bullet = Bullet(self.screen, self.x, self.y, -self.direction)
                self.shot_bullets.add(bullet)

                if len(self.shot_bullets.sprites()) == self.MAX_SHOT_BULLETS:
                    self.time_since_discharge = 0

    def kill(self):
        super().kill()
        # TODO(Victor) write kill
