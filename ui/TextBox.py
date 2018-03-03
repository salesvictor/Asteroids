import pygame


class TextBox:
    def __init__(self, center, font_size, dialogue):
        pygame.init()

        self.center = center
        self.font_size = font_size
        self.dialogue = dialogue

        self.font = pygame.font.Font("../fonts/Hyperspace.ttf", font_size)

        length = len(dialogue)
        self.size = (0.6*font_size*length, font_size)

        self.bg_color = (0, 0, 0)

    def process_input(self, events):
        pass

    def render(self, antialias, color, screen):
        pos = (self.center[0] - self.size[0]/2, self.center[1] - self.size[1]/2,
               self.size[0], self.size[1])

        screen.fill(self.bg_color, pos)
        text = self.font.render(self.dialogue, antialias, color)
        screen.blit(text, (pos[0], pos[1]))
