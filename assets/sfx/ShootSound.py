import os
import pygame as pg


class ShootSound():
    def __init__(self):
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'sounds', 'bullet.wav')
        shoot = pg.mixer.Sound(path)
        shoot.play()