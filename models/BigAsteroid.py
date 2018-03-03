import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.Asteroid import Asteroid

class BigAsteroid(Asteroid):

    def __init__(self, screen):
        super().__init__(screen, 0.4)

    def destroy(self):
        # TODO(Victor) write destroy
        pass
