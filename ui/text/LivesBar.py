import os
import pygame

class LivesBar:
    BG_COLOR = (0, 0, 0)
    BASE_LENGTH = 35
    BASE_HEIGHT = 20
    IMG_FACTOR = 0.075
    IMG_NAME = "ship.png"

    def __init__(self, center, lives):
        pygame.init()

        self.center = center
        self.lives = lives

        length = lives*self.BASE_LENGTH
        self.size = (length, self.BASE_HEIGHT)

        # Initializing ship image in graphics folder
        path = os.path.dirname(__file__)
        path = os.path.join(path, '..\\..\\assets\\graphics', self.IMG_NAME)
        original_image = pygame.image.load(path)
        self.original_image = pygame.transform.rotate(original_image, 90)

        # Resizing image
        img_size = self.original_image.get_rect().size
        new_img_size = []
        for dimension in img_size:
            new_img_size.append(int(self.IMG_FACTOR * dimension))
        self.original_image = pygame.transform.scale(self.original_image, new_img_size)
        self.image = self.original_image

    def update(self):
        length = self.lives*self.BASE_LENGTH
        self.size = (length, self.BASE_HEIGHT)

    def set_lives(self, lives):
        self.lives = lives
        self.update()

    def render(self, screen):
        pos = (self.center[0] - self.size[0]/2, self.center[1] - self.size[1]/2,
               self.size[0], self.size[1])

        screen.fill(self.BG_COLOR, pos)

        for i in range(self.lives):
            screen.blit(self.image, (pos[0]+self.BASE_LENGTH/4, pos[1]))
            pos = (pos[0]+self.BASE_LENGTH, pos[1])

