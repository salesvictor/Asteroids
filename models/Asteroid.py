import os
import sys
from math import cos, sin, radians
from random import randint

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.GameObject import GameObject

class Asteroid(GameObject):
    def __init__(self, screen, img_factor):
        """
        Description
        """
        # Generate a random position on the border for the asteroid to be
        # created
        x = 0
        y = 0
        i = randint(1, 4)
        if i == 1: # Left border
            y = randint(1, 639)
        elif i == 2: # Top border
            x = randint(1, 799)
        elif i == 3: # Right border
            x = 799
            y = randint(1, 639)
        else: # Bottom border
            x = randint(1, 799)
            y = 639

        # Generate velocity direction and speed
        asteroid_speed = randint(1, 5)
        angle = radians(randint(0, 360))
        asteroid_vel_dir = (cos(angle), sin(angle))

        super().__init__(x, y, 0, asteroid_vel_dir, asteroid_speed, screen,
                         'asteroid.png', img_factor)
