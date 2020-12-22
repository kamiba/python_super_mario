import pygame as pg
from .. import constants as c

class Mario(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = c.GFX['mario_bros']

        self.right_frames = []
        self.left_frames = []
        self.frame_index = 0
        self.load_from_sheet()
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()

    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()
        image.blit(self.sprite_sheet,(0,0),(x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width * c.SIZE_MULTIPLIER),
                                    int(rect.height * c.SIZE_MULTIPLIER)))
        return image

    def load_from_sheet(self):
        self.right_frames.append(self.get_image(178, 32, 12, 16))