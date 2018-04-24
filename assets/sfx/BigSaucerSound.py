import os
import pygame as pg


class BigSaucerSound():
    def __init__(self):
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'sounds', 'saucerBig.wav')
        big_saucer_sound = pg.mixer.Sound(path)
        big_saucer_sound.set_volume(0.01)
        big_saucer_sound.play()