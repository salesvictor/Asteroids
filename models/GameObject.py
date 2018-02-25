class GameObject:

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def on_border(self):
        if self.x < 0 or self.x > self.screen.width:
            self.x = (self.x + self.screen.width) % self.screen.width

        if self.y < 0 or self.y > self.screen.height:
            self.y = (self.y + self.screen.width) % self.screen.width

    def render(self):
        pass

    def destroy(self):
        pass
