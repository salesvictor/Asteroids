import pygame
from math import cos, sin, radians
from models.Ship import Ship

if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 800
    SCREEN_H = 600
    SIZE = (SCREEN_W, SCREEN_H)

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Ship Movement Testing')
    my_font = pygame.font.SysFont('Times New Roman', 15)
    clock = pygame.time.Clock()

    # Creates a sprite list for drawing
    sprites = pygame.sprite.Group()

    # Creates a new ship and adds it to the sprite list
    player = Ship(screen, SCREEN_W//2, SCREEN_H//2)
    sprites.add(player)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                break

        debug_text = (f'(pos, center, direction, speed, vel_dir) = '
                      f'(({player.x:3.0f}, {player.y:3.0f}), {player.rect.center}, '
                      f'{player.direction:3d}, {player.speed:3.2f}, '
                      f'({player.vel_dir[0]:3.2f}, {player.vel_dir[1]:3.2f}))')
        text_surface = my_font.render(debug_text, True, (255, 255, 255))
        (font_w, font_h) = text_surface.get_size()

        screen.fill((0, 0, 0))

        sprites.update()
        sprites.draw(screen)
        screen.blit(text_surface, ((SCREEN_W-font_w)/2, 0))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
