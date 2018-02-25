from random import randint
from models.GameObject import GameObject


class Asteroid(GameObject):

    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.type = randint(1,3)

    def render(self):
        # TODO(Victor) write render
        pass

    def destroy(self):
        # TODO(Victor) write destroy
        pass
