import pygame as pg

from text.TextBox import TextBox


class TextEntryBox(TextBox):
    DEFAULT_MAX_CHARACTERS = 6

    def __init__(self, screen, center, font_size, max_characters=DEFAULT_MAX_CHARACTERS):
        super().__init__(screen, center, font_size, '_'*max_characters)

        self.max_characters = max_characters

        # Store the real text entered by the player
        self.entered_text = ''

        # Flags to stop receiving characters and stop editing text
        self.has_max_characters = False
        self.poll = True

    def update(self, event):
        if len(self.entered_text) < self.max_characters:
            self.has_max_characters = False
        else:
            self.has_max_characters = True

        if self.poll:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.poll = False

                elif event.key == pg.K_BACKSPACE:
                    self.entered_text = self.entered_text[:-1]

                elif not self.has_max_characters:
                    self.entered_text += event.unicode

            self.dialogue = self.entered_text
            self.dialogue += '_' * (self.max_characters - len(self.entered_text))
            self.set_dialogue(self.dialogue)
