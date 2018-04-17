import pygame as pg
from ui.text.TextBox import TextBox


class TextButton(TextBox):
    def __init__(self, screen, center, font_size, dialogue=""):
        super().__init__(screen, center, font_size, dialogue)
        self.clicked = False
        self.selected = False

    def get_clicked(self):
        return self.clicked

    def contains_point(self, point):
        return (self.rect.center[0] - self.rect.size[0]/2 < point[0] < self.rect.center[0] + self.rect.size[0]/2 and
                self.rect.center[1] - self.rect.size[1]/2 < point[1] < self.rect.center[1] + self.rect.size[1]/2)

    def update(self, event):
        if event.type == pg.MOUSEMOTION:
            mouse_pos = event.dict["pos"]
            if self.contains_point(mouse_pos):
                self.selected = True
        else:
            self.selected = False

        if event.type == pg.MOUSEBUTTONDOWN:
            click_pos = event.dict["pos"]
            if self.contains_point(click_pos):
                self.clicked = True
        else:
            self.selected = False
