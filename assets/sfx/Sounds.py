import pygame as pg
import os


class Sounds:
    sound_param = 1

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
    def theme_song(cls, count):
        cls.path = os.path.dirname(__file__)
        sound1 = 0
        sound2 = 0
        if cls.sound_param == 1:
            sound1 = pg.mixer.Sound(os.path.join(cls.path, 'sounds', 'beat1.wav'))
            sound2 = pg.mixer.Sound(os.path.join(cls.path, 'sounds', 'beat2.wav'))
        elif cls.sound_param == 2:
            sound1 = pg.mixer.Sound(os.path.join(cls.path, 'sounds', 'beat1Danieel.wav'))
            sound2 = pg.mixer.Sound(os.path.join(cls.path, 'sounds', 'beat2Danieel.wav'))
        if cls.sound_param != 0:
            if 0 <= count <= 2:
                sound1.play()
            elif 45 <= count <= 47:
                sound2.play()

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
