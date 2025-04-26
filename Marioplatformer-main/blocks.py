import pygame as pg
import os

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__)

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface(
            (PLATFORM_WIDTH,
             PLATFORM_HEIGHT)
        )
        self.image.fill(pg.Color(PLATFORM_COLOR))
        self.image = pg.image.load("%s/blocks/platform.png" % ICON_DIR)
        self.rect = pg.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    