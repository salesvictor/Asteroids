import sys
import pygame

def main(args, fps, starting_scene):
    if args is None:
        size = (640, 480)
    elif len(args) == 2:
        size = (float(args[1]), float(args[2]))
    else:
        print('Usage:\n  main.py width heigth.\nExample:\n  main.py 640 480\n')
        return

    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed()

        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False

            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main(sys.argv[1:], 60, TitleScreen())
