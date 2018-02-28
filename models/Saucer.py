import random
import os
import sys
import pygame

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.GameObject import GameObject

class Saucer(GameObject):

    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)

        # Generating random number to chose if the saucer is big or small
        i = random.randint(0, 100)
        if i%2: # if i is even, saucer will be big
            factor = 0.8
        else:
            factor = 0.5

        # Initializing saucer image in graphics folder
        path = os.path.dirname(__file__)
        path = os.path.join(path, os.pardir, 'graphics', 'saucer.png')
        self.image = pygame.image.load(path)

        # Resizing image
        img_size = self.image.get_rect().size
        new_img_size = []
        for dimension in img_size:
            new_img_size.append(int(factor*dimension))
        self.image = pygame.transform.scale(self.image, new_img_size)

        # Use x and y as the dimensions of the image.
        self.rect = (x, y)

    def render(self):
        # TODO(Victor) write render
        pass

    def destroy(self):
        # TODO(Victor) write destroy
        pass
