import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.GameObject import GameObject


class Asteroid(GameObject):
    def __init__(self, x, y, screen, img_factor):
        super().__init__(x, y, 0, (0, 0), 0, screen, 'asteroid.png', img_factor)
