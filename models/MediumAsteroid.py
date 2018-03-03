import os
import sys
import pygame

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.GameObject import GameObject

class MediumAsteroid(GameObject):

    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)

        # Initializing asteroid image in graphics folder
        path = os.path.dirname(__file__)
        path = os.path.join(path, os.pardir, 'graphics', 'asteroid.png')
        self.image = pygame.image.load(path)

        # Resizing image
        img_size = self.image.get_rect().size
        new_img_size = []
        for dimension in img_size:
            new_img_size.append(int(0.25*dimension))
        self.image = pygame.transform.scale(self.image, new_img_size)

        # Use x and y as the dimensions of the image.
        self.rect = (x, y)

    def render(self):
        # TODO(Victor) write render
        pass

    def destroy(self):
        # TODO(Victor) write destroy
        pass
