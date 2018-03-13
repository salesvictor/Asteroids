from models.Ship import Ship

from ui.TextBox import TextBox
from ui.LivesBar import LivesBar


class Player(Ship):
    INITIAL_LIVES = 3
    MAX_LIVES = 5
    NAME_BOX_FONT_SIZE = 20
    SCORE_BOX_FONT_SIZE = 20

    def __init__(self, screen, x, y, number, initial_lives=INITIAL_LIVES):
        super().__init__(screen, x, y)
        self.initialx = x
        self.initialy = y

        self.lives = initial_lives
        self.score = 0
        self.number = number
        self.name = f"PLAYER{number}"
        self.screen = screen

        # Calculate position of text boxes and lives bar
        self.display_width_factor = screen.get_width() / 800
        self.display_height_factor = screen.get_height() / 640
        self.NAME_BOX_CENTER = (self.display_width_factor * 100, self.display_height_factor * 25)
        self.SCORE_BOX_CENTER = (self.NAME_BOX_CENTER[0], self.NAME_BOX_CENTER[1] + 25)
        self.LIVES_BAR_CENTER = (self.SCORE_BOX_CENTER[0], self.SCORE_BOX_CENTER[1] + 30)

        # Create text boxes and lives bar
        self.name_box = TextBox(self.NAME_BOX_CENTER, self.NAME_BOX_FONT_SIZE, self.name)
        self.score_box = TextBox(self.SCORE_BOX_CENTER, self.SCORE_BOX_FONT_SIZE, f"{self.score}")
        self.lives_bar = LivesBar(self.LIVES_BAR_CENTER, self.lives)

    def update(self, event=None):
        self.score_box.set_dialogue(f"{self.score}")

        super().update()

    def render(self):
        self.name_box.render(True, (255, 255, 255), self.screen)
        self.score_box.render(True, (255, 255, 255), self.screen)
        self.lives_bar.render(self.screen)

    def kill(self):
        groups = self.groups()

        super().kill()

        self.lives -= 1
        if self.lives == 0:
            self.lives_bar.set_lives(self.lives)

