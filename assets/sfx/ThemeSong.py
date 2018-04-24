import pygame as pg
import os


class ThemeSong():
    def __init__(self, count):
        path = os.path.dirname(__file__)
        sound1 = pg.mixer.Sound(os.path.join(path, 'sounds', 'beat1.wav'))
        sound2 = pg.mixer.Sound(os.path.join(path, 'sounds', 'beat2.wav'))
        if 0 <= count <= 2:
            sound1.play()
        elif 45 <= count <= 47:
            sound2.play()
