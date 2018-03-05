import pygame


class TextBox:
    BG_COLOR = (0, 0, 0)

    def __init__(self, center, font_size, dialogue):
        pygame.init()

        self.center = center
        self.font_size = font_size
        self.dialogue = dialogue

        self.font = pygame.font.Font("../fonts/Hyperspace.ttf", font_size)

        length = len(dialogue)
        self.size = (0.6*font_size*length, font_size)

    def set_dialogue(self, dialogue):
        self.dialogue = dialogue
        length = len(dialogue)
        self.size = (0.6*self.font_size*length, self.font_size)

    def render(self, antialias, color, screen):
        pos = (self.center[0] - self.size[0]/2, self.center[1] - self.size[1]/2,
               self.size[0], self.size[1])

        screen.fill(self.BG_COLOR, pos)

        text = self.font.render(self.dialogue, antialias, color)
        screen.blit(text, (pos[0], pos[1]))
