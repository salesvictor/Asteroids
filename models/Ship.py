import pygame as pg
from math import sqrt, cos, sin, radians
from models.GameObject import GameObject
from models.Bullet import Bullet


class Ship(GameObject):
    #  Movement constants
    ACCELERATION_MODULE = 0.2
    DEACCELERATION = 0.01
    MAX_SPEED = 3
    SHOT_DELAY = 10
    MAX_SHOT_BULLETS = 4
    RECHARGE_BULLETS_TIME = 70
    TURN_SPEED = -2

    def __init__(self, screen, x, y):
        super().__init__(x, y, -90, [0, 0], screen, 'ship.png', 0.1)
        self.shot_bullets = pg.sprite.Group()
        self.time_since_discharge = self.RECHARGE_BULLETS_TIME

    #  Update the ship and its bullets movement
    def update(self):
        speed_module = sqrt(self.speed[0]**2 + self.speed[1]**2)
        new_speed_module = max(speed_module - self.DEACCELERATION, 0)
        if self.speed[0] == 0:
            self.speed[0] = new_speed_module * cos(self.direction)
        else:
            self.speed[0] = self.speed[0] * new_speed_module / speed_module
        if self.speed[1] == 0:
            self.speed[1] = new_speed_module * sin(self.direction)
        else:
            self.speed[1] = self.speed[1] * new_speed_module / speed_module

        self.shot_bullets.update()

        self.time_since_discharge += 1

        super().update()

    # Make the ship go forward
    def forward(self):
        self.acceleration = [self.ACCELERATION_MODULE * cos(radians(self.direction)),
                             self.ACCELERATION_MODULE * sin(radians(self.direction))]
        self.speed = [self.speed[0] + self.acceleration[0], self.speed[1] + self.acceleration[1]]
        speed_module = sqrt(self.speed[0] ** 2 + self.speed[1] ** 2)
        new_speed_module = min(speed_module, self.MAX_SPEED)
        self.speed = [self.speed[0] * new_speed_module / speed_module, self.speed[1] * new_speed_module / speed_module]

    # Rotate the ship
    def turn(self, angle):
        self.image = pg.transform.rotate(self.original_image,
                                         -self.direction - angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.direction += angle

    #  Check for its bullets collisions and kill the objects colliding
    def check_bullets_collision(self, sprites_group):
        return pg.sprite.groupcollide(sprites_group, self.shot_bullets, True,
                                      True, pg.sprite.collide_mask)

    #  Check for player collisions with other objects
    def check_self_collision(self, sprites_group):
        collisions = pg.sprite.spritecollide(self, sprites_group, True,
                                             pg.sprite.collide_mask)
        if len(collisions) > 0:
            self.kill()
        return collisions

    #  Cast a bullet in the direction the ship is pointing
    def shoot(self):
        if self.time_since_discharge > self.RECHARGE_BULLETS_TIME:
            if len(self.shot_bullets.sprites()) == 0 or \
                (len(self.shot_bullets.sprites()) < self.MAX_SHOT_BULLETS and
                 self.shot_bullets.sprites()[-1].age > self.SHOT_DELAY):

                bullet = Bullet(self.screen, self.x, self.y, self.direction)
                self.shot_bullets.add(bullet)

                if len(self.shot_bullets.sprites()) == self.MAX_SHOT_BULLETS:
                    self.time_since_discharge = 0

    def kill(self):
        super().kill()