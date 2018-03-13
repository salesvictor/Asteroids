import pygame as pg

from ui.TextBox import TextBox


class TextEntryBox(TextBox):
    BG_COLOR = (0, 0, 0)

    def __init__(self, center, font_size, max_characters):
        pg.init()

        # Flags to stop receiving characters and stop editing text
        self.has_max_characters = False
        self.poll = True

        # Main attributes
        self.center = center
        self.font_size = font_size
        self.max_characters = max_characters
        self.dialogue = '_'*max_characters
        self.entered_text = ''

        self.font = pg.font.Font("../fonts/Hyperspace.ttf", font_size)

        self.size = (0.6*font_size*max_characters, font_size)

    def set_dialogue(self, dialogue):
        self.dialogue = dialogue
        length = len(dialogue)
        self.size = (0.6*self.font_size*length, self.font_size)

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

    def render(self, antialias, color, screen):
        pos = (self.center[0] - self.size[0]/2, self.center[1] - self.size[1]/2,
               self.size[0], self.size[1])

        screen.fill(self.BG_COLOR, pos)

        text = self.font.render(self.dialogue, antialias, color)
        screen.blit(text, (pos[0], pos[1]))
