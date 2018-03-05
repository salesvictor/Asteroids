import pygame

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

        # Create background asteroids
        self.asteroids = pygame.sprite.Group()
        for i in range(16):
            if i % 3 == 0:
                self.asteroids.add(SmallAsteroid(display))
            elif i % 3 == 1:
                self.asteroids.add(MediumAsteroid(display))
            else:
                self.asteroids.add(BigAsteroid(display))

    def process_input(self, events, pressed_keys):
        self.player.process_input(events, pressed_keys)

    def update(self):
        self.player.update()
        self.asteroids.update()

    def render(self):
        self.display.fill(self.BG_COLOR)
        self.player.render()
        self.asteroids.draw(self.display)
