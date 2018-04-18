import os
import pygame as pg


class BigSaucerSound():
    def __init__(self):
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'sounds', 'saucerBig.wav')
        big_explosion = pg.mixer.Sound(path)
        big_explosion.play()