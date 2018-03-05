class ScreenBase:
    BG_COLOR = (0, 0, 0)

    def __init__(self, display):
        self.next = self
        self.display = display

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)

