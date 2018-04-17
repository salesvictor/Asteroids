import sys
import pygame

from ui.screen.TitleScreen import TitleScreen


def main(args, fps):

    if not args:
        size = (800, 640)
    elif len(args) == 2:
        size = (float(args[1]), float(args[2]))
    else:
        print('Usage:\n  asteroids.py width heigth.\nExample:\n  asteroids.py 800 640\n')
        return

    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    active_scene = TitleScreen(screen)

    while active_scene is not None:
        # Process the filtered_events and update the frame
        event = active_scene.process_input()
        active_scene.update(event)
        active_scene.render()

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main(sys.argv[1:], 60)
