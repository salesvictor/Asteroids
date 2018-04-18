import pygame as pg
import os


class ThemeSong():
    def __init__(self):
        path = os.path.dirname(__file__)
        sound1 = pg.mixer.Sound(os.path.join(path, 'sounds', 'beat1.wav'))
        sound2 = pg.mixer.Sound(os.path.join(path, 'sounds', 'beat2.wav'))
        sound1.play()
        sound2.play()
