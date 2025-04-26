import pygame
from pygame import *
from pygame.constants import K_LEFT
from pygame.surface import Surface

from player import *
from blocks import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_conf(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera

    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width - WIN_WIDTH), l)
    t = min(0, t)
    t = max(-(camera.height - WIN_HEIGHT), t)

    return  Rect(l, t, w, h)

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Супер марио бойй")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

    hero = Player(55, 55)
    left = right = False
    up = False

    entites = pygame.sprite.Group()
    platforms = []

    entites.add(hero)

    level = [
        "----------------------------------",
        "-                                -",
        "-    ----               --       -",
        "-                                -",
        "-            --                  -",
        "-                    ------      -",
        "--                               -",
        "-                                -",
        "-                   ----     --- -",
        "-                                -",
        "--                               -",
        "-                                -",
        "-       -----                --- -",
        "-                                -",
        "-                                -",
        "-      ---                       -",
        "-                                -",
        "-   -------         ----         -",
        "-                                -",
        "-                         -      -",
        "-                            --  -",
        "-                                -",
        "-                                -",
        "----------------------------------"]

    timer = pygame.time.Clock()
    x = y = 0

    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entites.add(pf)

                platforms.append(pf)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT

    camera = Camera(camera_conf, total_level_width, total_level_height)

    while 1:
        timer.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit

            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w or event.key == K_SPACE:
                    up = True
                if event.key == K_RIGHT or event.key == K_d:
                    right = True
                if event.key == K_LEFT or event.key == K_a:
                    left = True

            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_w:
                    up = False
                if event.key == K_RIGHT or event.key == K_d:
                    right = False
                if event.key == K_LEFT or event.key == K_a:
                    left = False


        screen.blit(bg, (0, 0))

        camera.update(hero)

        hero.update(left, right, up, platforms)

        for e in entites:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

if __name__ == '__main__':
    main()