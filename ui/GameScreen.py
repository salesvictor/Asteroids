import pygame as pg

from ui.ScreenBase import ScreenBase
from player.UserPlayer import UserPlayer
from models.SmallAsteroid import SmallAsteroid
from models.MediumAsteroid import MediumAsteroid
from models.BigAsteroid import BigAsteroid


class GameScreen(ScreenBase):
    def __init__(self, display):
        super().__init__(display)

        # Create player
        self.player = UserPlayer(display, display.get_width()/2, display.get_height()/2, 1)
        self.players = pg.sprite.Group()
        self.players.add(self.player)

        # Create background asteroids
        self.asteroids = pg.sprite.Group()
        for i in range(16):
            if i % 3 == 0:
                self.asteroids.add(SmallAsteroid(display))
            elif i % 3 == 1:
                self.asteroids.add(MediumAsteroid(display))
            else:
                self.asteroids.add(BigAsteroid(display))

    def update(self, event):
        self.players.update(event)
        self.asteroids.update()

    def render(self):
        self.display.fill(self.BG_COLOR)
        for player in self.players:
            player.render()
        self.players.draw(self.display)
        for player in self.players:
            player.bullets_sprite.draw(self.display)
        self.asteroids.draw(self.display)
