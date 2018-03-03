import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import random
from models.GameObject import GameObject


class Saucer(GameObject):

    def __init__(self, x, y, screen):
        # Generating random number to chose if the saucer is big or small
        i = random.randint(0, 100)
        if i % 2 == 0:  # if i is even, saucer will be big
            factor = 0.6
        else:
            factor = 0.35

        super().__init__(x, y, 0, (0, 0), 0, screen, 'saucer.png', factor)

    def destroy(self):
        # TODO(Victor) write destroy
        pass
