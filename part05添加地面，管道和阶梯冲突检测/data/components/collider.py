import pygame as pg
from .. import constants as c

class Collider(pg.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width,height)).convert()
        self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

