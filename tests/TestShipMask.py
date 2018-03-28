import pygame as pg
from models.player.UserPlayer import UserPlayer


def change_color(screen):
    color = screen.get_at((0, 0))

    if color == (0, 0, 0):
        return (0, 0, 255)
    else:
        return (0, 0, 0)


if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 800
    SCREEN_H = 600
    SIZE = (SCREEN_W, SCREEN_H)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)

    bg_color = BLACK

    pg.init()
    pg.font.init()

    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption('Ship Movement Testing')
    my_font = pg.font.SysFont('Times New Roman', 20)
    clock = pg.time.Clock()

    # Creates a sprite list for drawing
    sprites = pg.sprite.Group()

    # Creates a new ship and adds it to the sprite list
    player = UserPlayer(screen, SCREEN_W//2, SCREEN_H//2, 1)
    sprites.add(player)

    while True:
        ev = pg.event.poll()
        if ev.type == pg.QUIT:
            break
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                break
            if ev.key == pg.K_SPACE:
                bg_color = change_color(screen)

        debug_text = (f'(pos, center, direction, speed, vel_dir) = '
                      f'(({player.x:3.0f}, {player.y:3.0f}), {player.rect.center}, '
                      f'{player.direction:3d}, {player.speed:3.2f}, '
                      f'({player.vel_dir[0]:3.2f}, {player.vel_dir[1]:3.2f}))')
        text_surface = my_font.render(debug_text, True, (255, 255, 255))
        (font_w, font_h) = text_surface.get_size()

        screen.fill(bg_color)

        sprites.update(ev)
        sprites.draw(screen)
        screen.blit(text_surface, ((SCREEN_W-font_w)/2, 0))

        # Get the outline of the mask then draw its points in the screen
        olist = player.mask.outline()
        true_olist = []
        for point in olist:
            true_point = (point[0] + player.rect.topleft[0], point[1] + player.rect.topleft[1])
            true_olist.append(true_point)

        pg.draw.polygon(screen, (200, 150, 150), true_olist, 0)

        pg.display.flip()
        clock.tick(FPS)


        pg.display.flip()
        clock.tick(FPS)

    pg.quit()
