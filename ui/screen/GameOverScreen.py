import pygame as pg

from ui.screen import GameScreen
from ui.screen.ScreenBase import ScreenBase
from ui.screen.HighScoresScreen import HighScoresScreen
from ui.screen.SettingsScreen import SettingsScreen
from score.ScoreCommunicator import ScoreCommunicator
from ui.text.TextBox import TextBox
from ui.text.TextEntryBox import TextEntryBox
from ui.text.TextButton import TextButton


class GameOverScreen(ScreenBase):
    SCREEN_TITLE_FONT_SIZE = 72
    PLAYER_NAME_ENTRY_BOX_FONT_SIZE = 36
    RETRY_BUTTON_FONT_SIZE = 24

    def __init__(self, display, players, remain_sprites):
        super().__init__(display)

        self.score_communicator = ScoreCommunicator('db/scores_db.csv')

        # Calculate position of game title and buttons
        self.display_width_factor = display.get_width() / 800
        self.display_height_factor = display.get_height() / 640
        self.SCREEN_TITLE_CENTER = (self.display_width_factor * 400, self.display_height_factor * 50)
        self.PLAYER_BOX_CENTER = (self.SCREEN_TITLE_CENTER[0],
                                  self.SCREEN_TITLE_CENTER[1] + self.display_height_factor * 200)
        self.PLAYER_NAME_ENTRY_BOX_CENTER = (self.PLAYER_BOX_CENTER[0],
                                             self.PLAYER_BOX_CENTER[1] + self.display_height_factor * 50)
        self.RETRY_BUTTON_CENTER = (self.PLAYER_NAME_ENTRY_BOX_CENTER[0],
                                    self.PLAYER_NAME_ENTRY_BOX_CENTER[1] + self.display_height_factor * 100)

        # Create screen title and buttons
        self.screen_title = TextBox(self.display, self.SCREEN_TITLE_CENTER, self.SCREEN_TITLE_FONT_SIZE, "GAME OVER")
        self.player_box = TextBox(self.display, self.PLAYER_BOX_CENTER, self.PLAYER_NAME_ENTRY_BOX_FONT_SIZE)
        self.player_name_entry_box = TextEntryBox(self.display, self.PLAYER_NAME_ENTRY_BOX_CENTER,
                                                  self.PLAYER_NAME_ENTRY_BOX_FONT_SIZE)
        self.retry_button = TextButton(self.display, self.RETRY_BUTTON_CENTER, self.RETRY_BUTTON_FONT_SIZE, "RETRY")

        # Receive players information
        self.players = []
        for player in players:
            self.players.append(player)

        # Create background with remaining game objects
        self.remain_sprites = remain_sprites

    def update(self, event):
        super().update(event)

        # If esc is pressed, switch to settings screen
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.switch_to_scene(SettingsScreen(self.display, self, self.remain_sprites))

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

        # If retry button is clicked, game is restarted ignoring actual player's name
        self.retry_button.update(event)

        if self.retry_button.get_clicked():
            self.switch_to_scene(GameScreen.GameScreen(self.display))

    # Render all text boxes and draw all sprites
    def render(self):
        self.display.fill(self.BG_COLOR)
        self.screen_title.render()
        self.player_box.render()
        self.player_name_entry_box.render()
        self.retry_button.render()
        self.remain_sprites.draw(self.display)
