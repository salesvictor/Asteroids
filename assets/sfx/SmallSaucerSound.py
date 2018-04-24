import os
import pygame as pg


class SmallSaucerSound():
    def __init__(self):
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'sounds', 'saucerSmall.wav')
        small_saucer_sound = pg.mixer.Sound(path)
        small_saucer_sound.set_volume(0.01)
        small_saucer_sound.play()