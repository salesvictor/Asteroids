import os
import pygame


class GameObject(pygame.sprite.Sprite):

    def __init__(self, x, y, direction, vel_dir, speed, screen, img_name, img_factor):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.screen = screen
        self.vel_dir = vel_dir
        self.direction = direction

        # Initializing ship image in graphics folder
        path = os.path.dirname(__file__)
        path = os.path.join(path, os.pardir, 'graphics', img_name)
        self.original_image = pygame.image.load(path)

        # Resizing image
        img_size = self.original_image.get_rect().size
        new_img_size = []
        for dimension in img_size:
            new_img_size.append(int(img_factor * dimension))
        self.original_image = pygame.transform.scale(self.original_image, new_img_size)
        self.image = self.original_image

        self.rect = self.image.get_rect(center=(x, y))

    def check_on_border(self):
        (width, height) = self.screen.get_size()

        if self.x < 0 or self.x > width:
            self.x = (self.x + width) % width

        if self.y < 0 or self.y > height:
            self.y = (self.y + height) % height

    def update(self):
        self.x += self.speed * self.vel_dir[0]
        self.y -= self.speed * self.vel_dir[1]
        self.direction = (self.direction + 360) % 360
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.check_on_border()

    def destroy(self):
        pass

    def get_vel_angle(self):
        pass