import os
import pygame as pg


class GameObject(pg.sprite.Sprite):

    def __init__(self, x, y, direction, speed, screen, img_name,
                 img_factor):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.screen = screen
        self.direction = direction

        # Initializing object image in graphics folder
        path = os.path.dirname(__file__)
        path = os.path.join(path, '..\\assets\\graphics', img_name)
        self.original_image = pg.image.load(path).convert()
        self.original_image.set_colorkey((0, 0, 0))

        # Resizing image
        img_size = self.original_image.get_rect().size
        new_img_size = []
        for dimension in img_size:
            new_img_size.append(int(img_factor * dimension))
        self.original_image = pg.transform.scale(self.original_image, new_img_size)

        self.image = self.original_image.copy()

        # Rotating and positioning image
        self.image = pg.transform.rotate(self.image, -direction)
        self.rect = self.image.get_rect(center=(x, y))

        # Creating mask
        self.mask_surface = self.image.copy()
        self.mask = pg.mask.from_surface(self.image)

    #  Make the object reappear in the opposite side of screen
    def check_on_border(self):
        (width, height) = self.screen.get_size()

        if self.rect.right < 0:
            self.rect.left = width
            (self.x, self.y) = self.rect.center
        if self.rect.left > width:
            self.rect.right = 0
            (self.x, self.y) = self.rect.center

        if self.rect.bottom < 0:
            self.rect.top = height
            (self.x, self.y) = self.rect.center
        if self.rect.top > height:
            self.rect.bottom = 0
            (self.x, self.y) = self.rect.center

    #  Movement updating of the object
    def update(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.center = (self.x, self.y)
        self.direction = (self.direction + 360) % 360
        self.check_on_border()

        # Updating masks with the inside area of the images
        self.mask_surface = self.image.copy()
        olist = self.mask.outline()
        mask_surface = self.image.copy()
        if len(olist) > 2:
            pg.draw.polygon(self.mask_surface, (200, 150, 150), olist, 0)
        self.mask = pg.mask.from_surface(mask_surface)

    def get_vel_angle(self):
        pass
