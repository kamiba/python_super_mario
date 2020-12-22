import os

import pygame as pg

from data.states import level1
from . import constants as c

def load_all_images(directory,colorkey=(255, 0, 255),accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img

    return graphics

class Control:
    def __init__(self):
        pg.init()
        pg.display.set_caption(c.ORIGINAL_CAPTION)
        self.screen = pg.display.set_mode(c.SCREEN_SIZE)
        self.done = False
        self.clock = pg.time.Clock()
        self.caption = c.ORIGINAL_CAPTION
        self.fps = 60
        self.show_fps = True
        self.keys = pg.key.get_pressed()
        c.GFX = load_all_images(os.path.join("resources", "graphics"))
        self.state = level1.Level1()

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
                self.toggle_show_fps(event.key)
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()

    def toggle_show_fps(self, key):
        if key == pg.K_F5:
            self.show_fps = not self.show_fps
    def update(self):
        self.state.update(self.screen)

    def main(self):
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)
            if self.show_fps:
                fps = self.clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
                pg.display.set_caption(with_fps)