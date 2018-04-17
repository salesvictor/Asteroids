import os
import pygame as pg


class TextBox(pg.sprite.Sprite):
    BG_COLOR = (0, 0, 0)
    TEXT_COLOR = (255, 255, 255)
    ANTIALIAS = True

    def __init__(self, screen, center, font_size, dialogue=""):
        pg.init()

        # Initializing the text, which is a drawable pygame Surface instance that uses font and dialogue
        # to render itself
        self.font_size = font_size
        path = os.path.dirname(__file__)
        path = os.path.join(path, os.pardir, os.pardir, 'assets', 'fonts', 'Hyperspace.ttf')
        path = open(path, 'rb')
        self.font = pg.font.Font(path, self.font_size)
        self.dialogue = dialogue
        self.text = self.font.render(self.dialogue, self.ANTIALIAS, self.TEXT_COLOR)

        # Initializing the rect that represents the box area
        size = (self.text.get_width(), self.text.get_height())
        self.rect = pg.Rect((center[0]-size[0]//2, center[1]-size[1]//2), size)

        self.screen = screen

    def set_dialogue(self, dialogue):
        self.dialogue = dialogue
        self.text = self.font.render(self.dialogue, self.ANTIALIAS, self.TEXT_COLOR)
        size = (self.text.get_width(), self.text.get_height())
        self.rect = pg.Rect((self.rect.center[0]-size[0]//2, self.rect.center[1]-size[1]//2), size)

    def update(self, event):
        pass

    def render(self):
        self.screen.fill(self.BG_COLOR, self.rect)
        self.screen.blit(self.text, self.rect.topleft)
