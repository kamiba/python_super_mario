from data.components import mario
from .. import constants as c
import pygame as pg
class Level1:
    def __init__(self):
        self.startup()

    def startup(self):
        self.mario = mario.Mario()
        self.setup_mario_location()
        self.all_sprites = pg.sprite.Group(self.mario)

    def setup_mario_location(self):
        self.mario.rect.x = 80
        self.mario.rect.bottom = c.SCREEN_HEIGHT - self.mario.rect.height

    def update(self,surface,keys,current_time):
        pg.display.get_surface().fill(c.BGCOLOR)
        self.all_sprites.update(keys,current_time)
        self.all_sprites.draw(surface)