from learning.TrainerScreen import TrainerScreen
from learning.SupervisedNetwork import ImitationNetwork
import sys
import os
import pygame as pg


def main(args, fps):
    if not args:
        size = (640, 480)
    elif len(args) == 2:
        size = (float(args[1]), float(args[2]))
    else:
        print('Usage:\n  asteroids.py width heigth.\nExample:\n  asteroids.py 800 640\n')
        return

    log_file_name = os.path.join(os.path.dirname(__file__), os.pardir, "db/player_log.csv")
    train_network = ImitationNetwork('trainer')
    train_network.fit(log_file_name)

    pg.mixer.pre_init(44100, -16, 2,  512)
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    active_scene = TrainerScreen(screen, ImitationNetwork)

    while active_scene is not None:
        # Process the filtered_events and update the frame
        event = active_scene.process_input()
        active_scene.update(event)
        active_scene.render()

        active_scene = active_scene.next

        pg.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main(sys.argv[1:], 60)
