import pygame as pg
import os
import time


class Sounds:
    sound_param = 1
    INITIAL_PERIOD = 1.0
    MIN_PERIOD = 0.2

    def __init__(self):
        self.theme_song_timer = time.clock()
        self.period = self.INITIAL_PERIOD
        self.beat = 0

    @classmethod
    def big_explosion_sound(cls):
        cls.path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            cls.path = os.path.join(cls.path, 'sounds', 'bigCollision.wav')
        elif cls.sound_param == 2:
            cls.path = os.path.join(cls.path, 'sounds', 'bigCollisionDanieel.wav')
        if cls.sound_param != 0:
            big_explosion = pg.mixer.Sound(cls.path)
            big_explosion.play()

    @classmethod
    def shoot_sound(cls):
        cls.path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            cls.path = os.path.join(cls.path, 'sounds', 'bullet.wav')
        elif cls.sound_param == 2:
            cls.path = os.path.join(cls.path, 'sounds', 'bulletDanieel.wav')
        if cls.sound_param != 0:
            shoot = pg.mixer.Sound(cls.path)
            shoot.play()

    @classmethod
    def small_saucer_sound(cls, sound_fader):
        cls.path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            cls.path = os.path.join(cls.path, 'sounds', 'saucerSmall.wav')
        elif cls.sound_param == 2:
            cls.path = os.path.join(cls.path, 'sounds', 'saucerSmallDanieel.wav')
        if cls.sound_param != 0:
            small_saucer_sound = pg.mixer.Sound(cls.path)
            small_saucer_sound.set_volume(sound_fader)
            small_saucer_sound.play()

    @classmethod
    def big_saucer_sound(cls, sound_fader):
        cls.path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            cls.path = os.path.join(cls.path, 'sounds', 'saucerBig.wav')
        elif cls.sound_param == 2:
            cls.path = os.path.join(cls.path, 'sounds', 'saucerBigDanieel.wav')
        if cls.sound_param != 0:
            big_saucer_sound = pg.mixer.Sound(cls.path)
            big_saucer_sound.set_volume(sound_fader)
            big_saucer_sound.play()

    @classmethod
    def small_explosion_sound(cls):
        cls.path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            cls.path = os.path.join(cls.path, 'sounds', 'smallCollision.wav')
        elif cls.sound_param == 2:
            cls.path = os.path.join(cls.path, 'sounds', 'smallCollisionDanieel.wav')
        if cls.sound_param != 0:
            small_explosion = pg.mixer.Sound(cls.path)
            small_explosion.play()

    @classmethod
    def medium_explosion_sound(cls):
        cls.path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            cls.path = os.path.join(cls.path, 'sounds', 'mediumCollision.wav')
        elif cls.sound_param == 2:
            cls.path = os.path.join(cls.path, 'sounds', 'mediumCollisionDanieel.wav')
        if cls.sound_param != 0:
            medium_explosion = pg.mixer.Sound(cls.path)
            medium_explosion.play()

    @classmethod
    def game_over(cls):
        cls.path = os.path.dirname(__file__)
        if cls.sound_param == 2:
            cls.path = os.path.join(cls.path, 'sounds', 'gameOverDanieel.wav')
            game_over = pg.mixer.Sound(cls.path)
            game_over.play()

    def theme_song(self):
        path = os.path.dirname(__file__)
        sound1 = 0
        sound2 = 0
        if self.sound_param == 1:
            sound1 = pg.mixer.Sound(os.path.join(path, 'sounds', 'beat1.wav'))
            sound2 = pg.mixer.Sound(os.path.join(path, 'sounds', 'beat2.wav'))
        elif self.sound_param == 2:
            sound1 = pg.mixer.Sound(os.path.join(path, 'sounds', 'beat1Danieel.wav'))
            sound2 = pg.mixer.Sound(os.path.join(path, 'sounds', 'beat2Danieel.wav'))
        if self.sound_param != 0:
            timer = time.clock()
            print(self.period)
            if timer - self.theme_song_timer > self.period:
                print(timer - self.theme_song_timer)
                if self.beat == 0:
                    sound1.play()
                elif self.beat == 1:
                    sound2.play()
                self.theme_song_timer = timer
                self.beat = (self.beat+1) % 2

    def set_period(self, new_period):
        self.period = max(self.MIN_PERIOD, new_period)
