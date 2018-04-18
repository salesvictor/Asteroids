import os
import pygame as pg


class MediumExplosionSound():
    def __init__(self):
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'sounds', 'mediumCollision.wav')
        medium_explosion = pg.mixer.Sound(path)
        medium_explosion.play()