import copy

from data.components import mario
from .. import constants as c
import pygame as pg
from data.components import collider


class Level1:
    def __init__(self):
        self.startup()

    def startup(self):
        self.mario = mario.Mario()
        self.setup_mario_location()
        self.all_sprites = pg.sprite.Group(self.mario)

        self.background = c.GFX['level_1']
        self.back_rect = self.background.get_rect()
        self.back_rect.x = 0
        self.back_rect.y = 0
        self.background = pg.transform.scale(self.background
                                             ,(int(self.back_rect.width*c.BACK_SIZE_MULTIPLER)
                                             ,int(self.back_rect.height*c.BACK_SIZE_MULTIPLER)))

        self.camera_adjust = 0
        self.setup_ground()
        self.setup_pipes()
        self.collide_group = pg.sprite.Group(self.ground_group
                                             ,self.pipe_group)

    def setup_pipes(self):
        self.pipe1 = collider.Collider(1202, 452, 83, 82)
        self.pipe2 = collider.Collider(1631, 409, 83, 140)
        self.pipe3 = collider.Collider(1973, 366, 83, 170)
        self.pipe4 = collider.Collider(2445, 366, 83, 170)
        self.pipe5 = collider.Collider(6989, 452, 83, 82)
        self.pipe6 = collider.Collider(7675, 452, 83, 82)

        self.pipe_group = pg.sprite.Group(self.pipe1, self.pipe2,
                                          self.pipe3, self.pipe4,
                                          self.pipe5, self.pipe6)

    def setup_ground(self):

        self.ground_rect1 = collider.Collider(0, c.GROUND_HEIGHT, 2953, 60)
        self.ground_rect2 = collider.Collider(3048, c.GROUND_HEIGHT, 635, 60)
        self.ground_rect3 = collider.Collider(3819, c.GROUND_HEIGHT, 2735, 60)
        self.ground_rect4 = collider.Collider(6647, c.GROUND_HEIGHT, 2300, 60)

        self.ground_group = pg.sprite.Group(self.ground_rect1,
                                            self.ground_rect2,
                                            self.ground_rect3,
                                            self.ground_rect4)

    def setup_mario_location(self):
        self.mario.rect.x = 80
        self.mario.rect.bottom = c.GROUND_HEIGHT

    def camera(self):
        if self.mario.rect.right > c.SCREEN_WIDTH / 3:
            self.camera_adjust = self.mario.rect.right - c.SCREEN_WIDTH / 3
        else:
            self.camera_adjust = 0

        self.back_rect.x -= self.camera_adjust

        for collider in self.collide_group:
            collider.rect.x -= self.camera_adjust

        for sprite in self.all_sprites:
            sprite.rect.x -= self.camera_adjust
            # print(sprite.rect.x)

    def update_mario_position(self):
        self.mario.rect.y += self.mario.y_vel
        collider = pg.sprite.spritecollideany(self.mario,self.collide_group)
        if collider:
            if self.mario.y_vel > 0:
                print(self.mario.rect)
                self.mario.y_vel = 0
                self.mario.state = c.WALK
                self.mario.rect.bottom = collider.rect.top
        else:
            test_sprite = copy.copy(self.mario)
            test_sprite.rect.y += 1
            if not pg.sprite.spritecollideany(test_sprite,self.collide_group):
                if self.mario.state != c.JUMP:
                    self.mario.state = c.FALL
            test_sprite.rect.y -= 1


        self.mario.rect.x += self.mario.x_vel

        if self.mario.rect.y > c.SCREEN_HEIGHT:
            self.startup()

        if self.mario.rect.x < 5:
            self.mario.rect.x = 5


    def update(self,surface,keys,current_time):
        # pg.display.get_surface().fill(c.BGCOLOR)
        surface.blit(self.background,self.back_rect)
        self.update_mario_position()
        self.all_sprites.update(keys,current_time)

        self.camera()
        self.all_sprites.draw(surface)
        self.ground_group.draw(surface)
        self.pipe_group.draw(surface)