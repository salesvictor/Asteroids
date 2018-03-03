from ScreenBase import *
from TextButton import *


class TitleScreen(ScreenBase):
    bg_color = (0, 0, 0)

    def __init__(self):
        super().__init__()

        game_title_center = (400, 200)
        game_title_font_size = 96
        play_button_center = (400, 350)
        score_button_center = (400, 400)
        button_font_size = 24

        self.game_title = TextBox(game_title_center, game_title_font_size, "ASTEROIDS")
        self.play_button = TextButton(play_button_center, button_font_size, "PLAY GAME")
        self.score_button = TextButton(score_button_center, button_font_size, "HIGH SCORES")

    def process_input(self, events, pressed_keys):
        self.play_button.process_input(events)
        if self.play_button.get_clicked():
            self.terminate()
            return

    def render(self, screen):
        # TODO: write actual redering
        bg_color = (0, 0, 0)

        screen.fill(bg_color)

        self.game_title.render(True, (255,255,255), screen)
        self.play_button.render(True, (255,255,255), screen)
        self.score_button.render(True, (255,255,255), screen)
