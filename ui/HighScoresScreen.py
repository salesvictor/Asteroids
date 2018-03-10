import pygame

from ui.ScreenBase import ScreenBase
# TODO: Check if there is a better way to deal with cyclic imports
import TitleScreen
from ui.TextBox import TextBox
from ui.TextButton import TextButton
from ui.ScoreCommunicator import ScoreCommunicator
from models.SmallAsteroid import SmallAsteroid
from models.MediumAsteroid import MediumAsteroid
from models.BigAsteroid import BigAsteroid


class HighScoresScreen(ScreenBase):
    SCREEN_TITLE_FONT_SIZE = 36
    BUTTON_FONT_SIZE = 24
    SCORE_FONT_SIZE = 24

    def __init__(self, display):
        super().__init__(display)

        # Calculate position of game title and buttons
        self.display_width_factor = display.get_width()/800
        self.display_height_factor = display.get_height()/640
        self.SCREEN_TITLE_CENTER = (self.display_width_factor*400, self.display_height_factor*50)
        self.BACK_BUTTON_CENTER = (self.SCREEN_TITLE_CENTER[0]-self.display_height_factor*250,
                                   self.SCREEN_TITLE_CENTER[1]+self.display_height_factor*50)
        self.CLEAR_SCORE_BUTTON_CENTER = (self.SCREEN_TITLE_CENTER[0]+self.display_height_factor*250,
                                          self.BACK_BUTTON_CENTER[1])
        self.FIRST_SCORE_BOX_CENTER = (self.SCREEN_TITLE_CENTER[0],
                                       self.CLEAR_SCORE_BUTTON_CENTER[1]+self.display_height_factor*50)

        # Create screen title and buttons
        self.screen_title = TextBox(self.SCREEN_TITLE_CENTER, self.SCREEN_TITLE_FONT_SIZE, "HIGH SCORES")
        self.back_button = TextButton(self.BACK_BUTTON_CENTER, self.BUTTON_FONT_SIZE, "BACK TO MENU")
        self.clear_score_button = TextButton(self.CLEAR_SCORE_BUTTON_CENTER, self.BUTTON_FONT_SIZE, "CLEAR SCORES")

        # Create vector of text boxes representing the scores table
        self.score_text_box = []

        # Create score communicator
        self.score_communicator = ScoreCommunicator("../db/score_db.csv")

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
        self.back_button.process_input(event)
        self.clear_score_button.process_input(event)

    def update(self, event):
        if self.back_button.get_clicked():
            self.switch_to_scene(TitleScreen.TitleScreen(self.display))
            return
        if self.clear_score_button.get_clicked():
            self.score_communicator.clear_db()
            print("ola")
            return

        self.score_communicator.read_csv_file()
        self.score_text_box = []
        rows_number = 0
        for row in self.score_communicator.scores_table:
            dialogue = row[0]
            for i in range(6 - len(row[0])):
                dialogue = dialogue + ' '
            for i in range(15):
                dialogue = dialogue + '. '
            dialogue = dialogue + '%05d' % row[1]
            center = (self.FIRST_SCORE_BOX_CENTER[0], self.FIRST_SCORE_BOX_CENTER[1]+rows_number*50)

            self.score_text_box.append(TextBox(center, self.SCORE_FONT_SIZE, dialogue))

            rows_number += 1
            if rows_number >= 10:
                break

        self.asteroids.update()

    def render(self):
        self.display.fill(self.BG_COLOR)

        self.screen_title.render(True, (255, 255, 255), self.display)
        self.back_button.render(True, (255, 255, 255), self.display)
        self.clear_score_button.render(True, (255, 255, 255), self.display)
        for text_box in self.score_text_box:
            text_box.render(True, (255, 255, 255), self.display)

        self.asteroids.draw(self.display)
