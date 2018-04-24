import os
import pygame as pg


class BigSaucerSound():
    def __init__(self, sound_fader):
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'sounds', 'saucerBig.wav')
        big_saucer_sound = pg.mixer.Sound(path)
        big_saucer_sound.set_volume(sound_fader)
        big_saucer_sound.play()
