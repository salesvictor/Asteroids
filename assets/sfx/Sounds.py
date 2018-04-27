import pygame as pg
import os
import time


class Sounds:
    playing = False
    sound_param = 1
    INITIAL_PERIOD = 1.0
    MIN_PERIOD = 0.25

    def __init__(self):
        self.theme_song_timer = time.clock()
        self.period = self.INITIAL_PERIOD
        self.beat = 0

    @classmethod
    def big_explosion_sound(cls):
        path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            path = os.path.join(path, 'sounds', 'bigCollision.wav')
        elif cls.sound_param == 2:
            path = os.path.join(path, 'sounds', 'bigCollisionDanieel.wav')
        if cls.sound_param != 0:
            big_explosion = pg.mixer.Sound(path)
            big_explosion.play()

    @classmethod
    def shoot_sound(cls):
        path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            path = os.path.join(path, 'sounds', 'bullet.wav')
        elif cls.sound_param == 2:
            path = os.path.join(path, 'sounds', 'bulletDanieel.wav')
        if cls.sound_param != 0:
            shoot = pg.mixer.Sound(path)
            shoot.play()

    @classmethod
    def small_saucer_sound(cls, sound_fader):
        path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            path = os.path.join(path, 'sounds', 'saucerSmall.wav')
        elif cls.sound_param == 2:
            path = os.path.join(path, 'sounds', 'saucerSmallDanieel.wav')
        if cls.sound_param != 0:
            small_saucer_sound = pg.mixer.Sound(path)
            small_saucer_sound.set_volume(sound_fader)
            small_saucer_sound.play()

    @classmethod
    def big_saucer_sound(cls, sound_fader):
        path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            path = os.path.join(path, 'sounds', 'saucerBig.wav')
        elif cls.sound_param == 2:
            path = os.path.join(path, 'sounds', 'saucerBigDanieel.wav')
        if cls.sound_param != 0:
            big_saucer_sound = pg.mixer.Sound(path)
            big_saucer_sound.set_volume(sound_fader)
            big_saucer_sound.play()

    @classmethod
    def small_explosion_sound(cls):
        path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            path = os.path.join(path, 'sounds', 'smallCollision.wav')
        elif cls.sound_param == 2:
            path = os.path.join(path, 'sounds', 'smallCollisionDanieel.wav')
        if cls.sound_param != 0:
            small_explosion = pg.mixer.Sound(path)
            small_explosion.play()

    @classmethod
    def medium_explosion_sound(cls):
        path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            path = os.path.join(path, 'sounds', 'mediumCollision.wav')
        elif cls.sound_param == 2:
            path = os.path.join(path, 'sounds', 'mediumCollisionDanieel.wav')
        if cls.sound_param != 0:
            medium_explosion = pg.mixer.Sound(path)
            medium_explosion.play()

    @classmethod
    def game_over(cls):
        path = os.path.dirname(__file__)
        if cls.sound_param == 1:
            path = os.path.join(path, 'sounds', 'gameOver.wav')
        elif cls.sound_param == 2:
            path = os.path.join(path, 'sounds', 'gameOverDanieel.wav')
        if cls.sound_param != 0:
            game_over = pg.mixer.Sound(path)
            game_over.play()

    @classmethod
    def play_title_song(cls):
        if cls.sound_param != 0 and not cls.playing:
            path = os.path.dirname(__file__)
            path = os.path.join(path, 'sounds', 'interstellarTheme.wav')
            pg.mixer.music.load(path)
            pg.mixer.music.play(-1)
            cls.playing = True

    @classmethod
    def pause_title_song(cls):
        pg.mixer.music.pause()

    @classmethod
    def unpause_title_song(cls):
        pg.mixer.music.unpause()

    @classmethod
    def stop_title_song(cls):
        pg.mixer.music.stop()
        cls.playing = False

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
            if timer - self.theme_song_timer > self.period:
                if self.beat == 0:
                    sound1.play()
                elif self.beat == 1:
                    sound2.play()
                self.theme_song_timer = timer
                self.beat = (self.beat+1) % 2

    def set_period(self, new_period):
        self.period = max(self.MIN_PERIOD, new_period)
