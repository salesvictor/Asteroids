import pygame

from ui.ScreenBase import ScreenBase
from ui.GameScreen import GameScreen
# TODO: Check if there is a better way to deal with cyclic imports
import HighScoresScreen
from ui.TextBox import TextBox
from ui.TextButton import TextButton
from models.SmallAsteroid import SmallAsteroid
from models.MediumAsteroid import MediumAsteroid
from models.BigAsteroid import BigAsteroid


class TitleScreen(ScreenBase):
    GAME_TITLE_FONT_SIZE = 96
    BUTTON_FONT_SIZE = 24

    def __init__(self, display):
        super().__init__(display)

        # Calculate position of game title and buttons
        self.display_width_factor = display.get_width()/800
        self.display_height_factor = display.get_height()/640
        self.GAME_TITLE_CENTER = (self.display_width_factor*400, self.display_height_factor*200)
        self.PLAY_BUTTON_CENTER = (self.GAME_TITLE_CENTER[0], self.GAME_TITLE_CENTER[1]+self.display_height_factor*150)
        self.SCORE_BUTTON_CENTER = (self.PLAY_BUTTON_CENTER[0], self.PLAY_BUTTON_CENTER[1]+50)

        # Create game title and buttons
        self.game_title = TextBox(self.GAME_TITLE_CENTER, self.GAME_TITLE_FONT_SIZE, "ASTEROIDS")
        self.play_button = TextButton(self.PLAY_BUTTON_CENTER, self.BUTTON_FONT_SIZE, "PLAY GAME")
        self.score_button = TextButton(self.SCORE_BUTTON_CENTER, self.BUTTON_FONT_SIZE, "HIGH SCORES")

        # Create background asteroids
        self.asteroids = pygame.sprite.Group()
        for i in range(12):
            if i % 3 == 0:
                self.asteroids.add(SmallAsteroid(display))
            elif i % 3 == 1:
                self.asteroids.add(MediumAsteroid(display))
            else:
                self.asteroids.add(BigAsteroid(display))

    def process_input(self):
        event = super().process_input()
        self.play_button.process_input(event)
        self.score_button.process_input(event)

    def update(self, event):
        if self.play_button.get_clicked():
            self.switch_to_scene(GameScreen(self.display))
            return

        if self.score_button.get_clicked():
            self.switch_to_scene(HighScoresScreen.HighScoresScreen(self.display))

        self.asteroids.update()

    def render(self):
        self.display.fill(self.BG_COLOR)

        self.game_title.render(True, (255, 255, 255), self.display)
        self.play_button.render(True, (255, 255, 255), self.display)
        self.score_button.render(True, (255, 255, 255), self.display)

        self.asteroids.draw(self.display)
