from random import randint

from models.Saucer import Saucer
from models.Bullet import Bullet
from assets.sfx.Sounds import Sounds


class BigSaucer(Saucer):

    def __init__(self, screen, x=None, y=None, speed=None, vel_dir=None):
        self.bullet_timer = 0
        self.sound_fader = 1
        super().__init__(screen, 'big_saucer.png', 0.7, x, y, speed, vel_dir)

    def shoot(self):
        self.direction = randint(0, 360)
        bullet = Bullet(self.screen, self.x, self.y, self.direction)
        self.saucer_shot_bullets.add(bullet)

    def update(self):
        self.bullet_timer = (self.bullet_timer + 1) % 50
        if self.bullet_timer == 25:
            self.shoot()
        
        super().update()

        # Decreases sound_fader on each frame
        self.sound_fader = self.sound_fader / 1.035
        Sounds.big_saucer_sound(self.sound_fader)
