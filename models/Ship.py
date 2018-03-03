import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pygame
from models.GameObject import GameObject
from models.Bullet import Bullet

class Ship(GameObject):
    ACCEL = 0.2
    DEACCEL = 0.02
    MAX_SPEED = 4.5
    SHOT_DELAY = 5

    def __init__(self, screen, x, y):
        super().__init__(x, y, 0, (0, 0), 0, screen, 'ship.png', 0.1)
        self.shot_bullets = []

    def update(self):
        self.x += self.speed * self.vel_dir[0]
        self.y -= self.speed * self.vel_dir[1]
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.check_on_border()

    def turn(self, angle):
        self.image = pygame.transform.rotate(self.original_image, self.direction + angle)
        self.direction += angle
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def accelerate(self, vel_dir):
        self.speed = min(self.speed+self.ACCEL, self.MAX_SPEED)
        self.vel_dir = vel_dir

    def stop(self):
        self. speed = max(self.speed-self.DEACCEL, 0)

    def shot(self):
        if len(self.shot_bullets) == 0 or self.shot_bullets[-1].age > self.SHOT_DELAY:
            bullet = Bullet(self.screen, self.x, self.y, -self.direction)
            self.shot_bullets.append(bullet)

    def destroy(self):
        # TODO(Victor) write destroy
        pass
