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

        self.background = c.GFX['level_1']
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background
                                             ,(int(self.back_rect.width*c.BACK_SIZE_MULTIPLER)
                                             ,int(self.back_rect.height*c.BACK_SIZE_MULTIPLER)))

        self.camera_adjust = 0

    def setup_mario_location(self):
        self.mario.rect.x = 80
        self.mario.rect.bottom = c.SCREEN_HEIGHT - c.GROUND_HEIGHT

    def camera(self):
        if self.mario.rect.right > c.SCREEN_WIDTH / 3:
            self.camera_adjust = self.mario.rect.right - c.SCREEN_WIDTH / 3
        else:
            self.camera_adjust = 0

        self.back_rect.x -= self.camera_adjust
        # print(self.camera_adjust)
        # print(self.back_rect.x)

        for sprite in self.all_sprites:
            sprite.rect.x -= self.camera_adjust
            print(sprite.rect.x)

    def update(self,surface,keys,current_time):
        # pg.display.get_surface().fill(c.BGCOLOR)
        surface.blit(self.background,self.back_rect)
        self.all_sprites.update(keys,current_time)
        self.camera()
        self.all_sprites.draw(surface)