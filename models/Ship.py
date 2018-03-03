import os
import sys
import pygame

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.GameObject import GameObject

class Ship(GameObject):
    ACCEL = 0.5
    DEACCEL = 0.1
    MAX_SPEED = 5

    def __init__(self, screen, x, y):
        # super().__init__(screen.width//2, screen.height//2, (0, 0), screen)
        super().__init__(x, y, 0, (0, 0), 0, screen, 'ship.png', 0.1)
        self.speed = 0

    def turn(self, angle):
        self.image = pygame.transform.rotate(self.original_image, self.direction + angle)
        self.direction += angle
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def accelerate(self, vel_dir):
        self.speed = min(self.speed+self.ACCEL, self.MAX_SPEED)
        self.vel_dir = vel_dir

    def stop(self):
        self. speed = max(self.speed-self.DEACCEL, 0)

    def destroy(self):
        # TODO(Victor) write destroy
        pass
