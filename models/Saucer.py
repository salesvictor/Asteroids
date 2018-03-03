import random
import os
import sys
import pygame

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.GameObject import GameObject

class Saucer(GameObject):

    def __init__(self, x, y, screen):
        # Generating random number to chose if the saucer is big or small
        i = random.randint(0, 100)
        if i%2: # if i is even, saucer will be big
            factor = 0.6
        else:
            factor = 0.35

        super().__init__(x, y, 0, (0, 0), 0, screen, 'saucer.png', factor)

    def render(self):
        # TODO(Victor) write render
        pass

    def destroy(self):
        # TODO(Victor) write destroy
        pass
