import pygame as pg

from ui.ScreenBase import ScreenBase
from ui.HighScoresScreen import HighScoresScreen
from ui.ScoreCommunicator import ScoreCommunicator
from ui.TextBox import TextBox
from ui.TextEntryBox import TextEntryBox
from ui.TextButton import TextButton


class GameOverScreen(ScreenBase):
    SCREEN_TITLE_FONT_SIZE = 72
    PLAYER_NAME_ENTRY_BOX_FONT_SIZE = 36
    BUTTON_FONT_SIZE = 24
    PLAYER_NAME_ENTRY_BOX_MAX_CHARACTERS = 6

    def __init__(self, display, players, remain_sprites):
        super().__init__(display)

        self.score_communicator = ScoreCommunicator('../db/scores_db.csv')

        # Calculate position of game title and buttons
        self.display_width_factor = display.get_width() / 800
        self.display_height_factor = display.get_height() / 640
        self.SCREEN_TITLE_CENTER = (self.display_width_factor * 400, self.display_height_factor * 50)
        self.PLAYER_BOX_CENTER = (self.SCREEN_TITLE_CENTER[0],
                              self.SCREEN_TITLE_CENTER[1] + self.display_height_factor * 200)
        self.PLAYER_NAME_ENTRY_BOX_CENTER = (self.PLAYER_BOX_CENTER[0],
                                             self.PLAYER_BOX_CENTER[1] + self.display_height_factor * 50)

        # Create screen title and buttons
        self.screen_title = TextBox(self.SCREEN_TITLE_CENTER, self.SCREEN_TITLE_FONT_SIZE, "GAME OVER")
        self.player_box = TextBox(self.PLAYER_BOX_CENTER, self.PLAYER_NAME_ENTRY_BOX_FONT_SIZE, "")
        self.player_name_entry_box = TextEntryBox(self.PLAYER_NAME_ENTRY_BOX_CENTER,
                                                  self.PLAYER_NAME_ENTRY_BOX_FONT_SIZE,
                                                  self.PLAYER_NAME_ENTRY_BOX_MAX_CHARACTERS)

        # Receive players information
        self.players = []
        for player in players:
            self.players.append(player)

        # Create background with remaining game objects
        self.remain_sprites = remain_sprites

    def update(self, event):
        # Update objects movement
        self.remain_sprites.update()

        # Update player names entry system
        if len(self.players) != 0:
            player_box_dialogue = f'ENTER PLAYER{self.players[0].number} NAME:'
            self.player_box.set_dialogue(player_box_dialogue)

            self.player_name_entry_box.update(event)

            if not self.player_name_entry_box.poll:
                self.players[0].name = self.player_name_entry_box.entered_text
                self.score_communicator.write_csv_file(self.players[0].name, self.players[0].score)
                self.players.remove(self.players[0])

        # If all players received a name, end the screen
        else:
            self.switch_to_scene(HighScoresScreen(self.display))

    # Render all text boxes and draw all sprites
    def render(self):
        self.display.fill(self.BG_COLOR)
        self.screen_title.render(True, (255, 255, 255), self.display)
        self.player_box.render(True, (255, 255, 255), self.display)
        self.player_name_entry_box.render(True, (255, 255, 255), self.display)
        self.remain_sprites.draw(self.display)
