import pygame as pg
import os


class ThemeSong():
    def __init__(self, count):
        path = os.path.dirname(__file__)
        sound1 = pg.mixer.Sound(os.path.join(path, 'sounds', 'beat1.wav'))
        sound2 = pg.mixer.Sound(os.path.join(path, 'sounds', 'beat2.wav'))
        if count == 1:
            sound1.play()
        elif count == 31:
            sound2.play()
