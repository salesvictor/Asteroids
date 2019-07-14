import pygame as pg

from ui.screen.ScreenBase import ScreenBase
from ui.text.TextBox import TextBox
from ui.text.TextButton import TextButton
from assets.sfx.Sounds import Sounds
from ui.screen import TitleScreen


class SettingsScreen(ScreenBase):
    SCREEN_TITLE_FONT_SIZE = 48
    SOUND_BUTTON_FONT_SIZE = 36
    OPTIONS_FONT_SIZE = 24
    RESUME_BUTTON_FONT_SIZE = 24
    MENU_SIZE = (600, 500)

    def __init__(self, display, previous_scene, remain_sprites):
        super().__init__(display)

        # Calculate position of game title and buttons
        self.display_width_factor = display.get_width() / 800
        self.display_height_factor = display.get_height() / 640
        self.SCREEN_TITLE_CENTER = (self.display_width_factor * 400, self.display_height_factor * 100)
        self.SOUND_OPTIONS_CENTER = (self.display_width_factor * 400, self.display_height_factor * 200)
        self.DEFAULT_CENTER = (self.display_width_factor * 250, self.display_height_factor * 250)
        self.BONUS_CENTER = (self.display_width_factor * 400, self.display_height_factor * 250)
        self.MUTE_CENTER = (self.display_width_factor * 550, self.display_height_factor * 250)
        self.RESUME_BUTTON_CENTER = (self.SCREEN_TITLE_CENTER[0],
                                     self.SCREEN_TITLE_CENTER[1] + self.display_height_factor * 250)
        self.LOG_CENTER = (self.RESUME_BUTTON_CENTER[0],
                           self.RESUME_BUTTON_CENTER[1] + self.display_height_factor * 100)
        self.MAIN_MENU_CENTER = (self.LOG_CENTER[0],
                                 self.LOG_CENTER[1] + self.display_height_factor * 100)

        # Create screen title and buttons
        self.screen_title = TextBox(self.display, self.SCREEN_TITLE_CENTER, self.SCREEN_TITLE_FONT_SIZE, "SETTINGS")
        self.sound_options = TextBox(self.display, self.SOUND_OPTIONS_CENTER, self.SOUND_BUTTON_FONT_SIZE,
                                     "SOUND OPTIONS")
        self.default = TextButton(self.display, self.DEFAULT_CENTER, self.OPTIONS_FONT_SIZE, "DEFAULT")
        self.bonus = TextButton(self.display, self.BONUS_CENTER, self.OPTIONS_FONT_SIZE, "BONUS")
        self.none = TextButton(self.display, self.MUTE_CENTER, self.OPTIONS_FONT_SIZE, "MUTE")
        self.resume_button = TextButton(self.display, self.RESUME_BUTTON_CENTER, self.RESUME_BUTTON_FONT_SIZE, "RESUME")
        self.log_button = TextButton(self.display, self.LOG_CENTER, self.RESUME_BUTTON_FONT_SIZE, "LOG")
        self.main_menu_button = TextButton(self.display, self.MAIN_MENU_CENTER, self.RESUME_BUTTON_FONT_SIZE,
                                           "MAIN MENU")

        # Create a rect to fill with nothing but the settings menu
        self.menu_rect = pg.Rect(self.display.get_width()/2 - self.display_height_factor * self.MENU_SIZE[0]/2,
                                 self.display.get_height()/2 - self.display_height_factor * self.MENU_SIZE[1]/2,
                                 self.MENU_SIZE[0], self.MENU_SIZE[1])

        # Store previous scene for later callback
        self.previous_scene = previous_scene

        # Create background with remaining game objects
        self.remain_sprites = remain_sprites

    def update(self, event):
        super().update(event)

        # If esc is pressed, switch to previous scene
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.switch_to_scene(self.previous_scene)

        # If default is pressed change sound_param
        self.default.update(event)
        if self.default.get_clicked():
            Sounds.sound_param = 1
            Sounds.unpause_title_song()

        # If bonus is pressed change sound_param
        self.bonus.update(event)
        if self.bonus.get_clicked():
            Sounds.sound_param = 2
            Sounds.unpause_title_song()

        # If none is pressed change sound_param
        self.none.update(event)
        if self.none.get_clicked():
            Sounds.sound_param = 0
            Sounds.pause_title_song()

        # If resume button is clicked, back to the previous scene
        self.resume_button.update(event)
        if self.resume_button.get_clicked():
            self.switch_to_scene(self.previous_scene)

        # If log button is clicked, switch logging state of previous scene, if possible
        self.log_button.update(event)
        if self.log_button.get_clicked():
            if self.previous_scene.__class__.__name__ == "GameScreen":
                self.previous_scene.logging = not self.previous_scene.logging

        # If main menu button is clicked, switches to title screen
        self.main_menu_button.update(event)
        if self.main_menu_button.get_clicked():
            self.switch_to_scene(TitleScreen.TitleScreen(self.display))

    # Render all text boxes and draw all sprites
    def render(self):
        self.display.fill(self.BG_COLOR)
        self.remain_sprites.draw(self.display)
        self.display.fill(self.BG_COLOR, self.menu_rect)
        self.screen_title.render()
        self.sound_options.render()
        self.default.render()
        self.bonus.render()
        self.none.render()
        self.resume_button.render()
        self.log_button.render()
        self.main_menu_button.render()
