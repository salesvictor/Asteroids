from TextBox import TextBox


class TextButton(TextBox):
    def __init__(self, center, font_size, dialogue):
        super().__init__(center, font_size, dialogue)
        self.clicked = False

    def contains_point(self, point):
        return (self.center[0] - self.size[0]/2 < point[0] < self.center[0] + self.size[0]/2 and
                self.center[1] - self.size[1]/2 < point[1] < self.center[1] + self.size[1]/2)

    def process_input(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.dict["pos"]
                if self.contains_point(click_pos):
                    self.clicked = True

    def get_clicked(self):
        return self.clicked
