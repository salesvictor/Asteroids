import pygame as pg

from screen.ScreenBase import ScreenBase
from text.TextBox import TextBox
from text.TextButton import TextButton


class SettingsScreen(ScreenBase):
    SCREEN_TITLE_FONT_SIZE = 48
    RESUME_BUTTON_FONT_SIZE = 24
    MENU_SIZE = (600, 500)

    def __init__(self, display, previous_scene, remain_sprites):
        super().__init__(display)

        # Calculate position of game title and buttons
        self.display_width_factor = display.get_width() / 800
        self.display_height_factor = display.get_height() / 640
        self.SCREEN_TITLE_CENTER = (self.display_width_factor * 400, self.display_height_factor * 100)
        self.PLAYER_BOX_CENTER = (self.SCREEN_TITLE_CENTER[0],
                                  self.SCREEN_TITLE_CENTER[1] + self.display_height_factor * 200)
        self.RESUME_BUTTON_CENTER = (self.SCREEN_TITLE_CENTER[0],
                                     self.SCREEN_TITLE_CENTER[1] + self.display_height_factor * 200)

        # Create screen title and buttons
        self.screen_title = TextBox(self.display, self.SCREEN_TITLE_CENTER, self.SCREEN_TITLE_FONT_SIZE, "SETTINGS")
        self.resume_button = TextButton(self.display, self.RESUME_BUTTON_CENTER, self.RESUME_BUTTON_FONT_SIZE, "RESUME")

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

        # If resume button is clicked, back to the previous scene
        self.resume_button.update(event)
        if self.resume_button.get_clicked():
            self.switch_to_scene(self.previous_scene)

    # Render all text boxes and draw all sprites
    def render(self):
        self.display.fill(self.BG_COLOR)
        self.remain_sprites.draw(self.display)
        self.display.fill(self.BG_COLOR, self.menu_rect)
        self.screen_title.render()
        self.resume_button.render()
