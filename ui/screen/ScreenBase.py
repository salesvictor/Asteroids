import pygame as pg


class ScreenBase:
    BG_COLOR = (0, 0, 0)

    def __init__(self, display):
        self.next = self
        self.display = display

    def process_input(self):
        event = pg.event.poll()
        pressed_keys = pg.key.get_pressed()

        if event.type == pg.QUIT:
            self.terminate()
        elif event.type == pg.KEYDOWN:
            alt_pressed = pressed_keys[pg.K_LALT] or \
                          pressed_keys[pg.K_RALT]
            if event.key == pg.K_ESCAPE:
                self.terminate()
            elif event.key == pg.K_F4 and alt_pressed:
                self.terminate()

        return event

    def update(self, event):
        pass

    def render(self):
        pass

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)

