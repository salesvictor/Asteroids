import pygame as pg
from math import atan, degrees, pi
from models.Bullet import Bullet

if __name__ == '__main__':
    FPS = 60
    SCREEN_W = 800
    SCREEN_H = 600
    SIZE = (SCREEN_W, SCREEN_H)
    BLACK = (0, 0, 0)

    pg.init()
    pg.font.init()

    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption('Bullet Creation Test')
    my_font = pg.font.SysFont('Times New Roman', 20)
    clock = pg.time.Clock()

    # Creates a sprite list for drawing
    sprites = pg.sprite.Group()

    while True:
        ev = pg.event.poll()
        if ev.type == pg.QUIT:
            break
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                break
        elif ev.type == pg.MOUSEBUTTONDOWN:
            # Creates a new bullet to go through the clicked direction and adds it to the sprite list
            click_pos = ev.dict["pos"]
            direction = atan((click_pos[1]-SCREEN_H/2) / (click_pos[0]-SCREEN_W/2))
            if click_pos[0] < SCREEN_W/2:
                direction += pi

            direction = degrees(direction)

            print(direction)

            bullet = Bullet(screen, SCREEN_W/2, SCREEN_H/2, direction)
            sprites.add(bullet)

        debug_text = f"Bullets Directions: {[float(f'{bullet.direction:3.2f}') for bullet in sprites]}"
        text_surface = my_font.render(debug_text, True, (255, 255, 255))
        (font_w, font_h) = text_surface.get_size()

        screen.fill(BLACK)

        sprites.update()
        sprites.draw(screen)

        # Get the outline of the mask then draw its points in the screen
        for bullet in sprites:
            olist = bullet.mask.outline()
            true_olist = []
            for point in olist:
                true_point = (point[0] + bullet.rect.topleft[0], point[1] + bullet.rect.topleft[1])
                true_olist.append(true_point)

            if len(true_olist) > 2:
                pg.draw.polygon(screen, (200, 150, 150), true_olist, 0)

        screen.blit(text_surface, ((SCREEN_W-font_w)/2, 0))
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()
