import os
import pygame as pg


class SmallExplosionSound():
    def __init__(self):
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'sounds', 'smallCollision.wav')
        small_explosion = pg.mixer.Sound(path)
        small_explosion.play()