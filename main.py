import pygame as pg
import os
import sys
import random

from letter_images import *
from settings import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

        self.game_state = 0

    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        if self.game_state == 0:
            font_start = pg.font.Font('freesansbold.ttf', 46)
            text_start = font_start.render('Press Mouse Button To Start', True, 'black', 'white')
            text_start_rect = text_start.get_rect()
            text_start_rect.center = (RES[0]//2, RES[1]//2)
            self.screen.blit(text_start, text_start_rect)

        elif self.game_state == 1:
            pass

        elif self.game_state == 2:
            self.screen.fill('black')
            i = random.randrange(0, 23, 1)
            r1 = random.randrange(0, 23, 1)
            r2 = random.randrange(0, 23, 1)
            r3 = random.randrange(0, 23, 1)
            r4 = random.randrange(0, 23, 1)

            letter_rect = alphabet[i][(i % 2)].get_rect()
            letter_rect.center = (RES[0]//2, 200)

            self.screen.blit(alphabet[i][(i % 2)], letter_rect)

            font1 = pg.font.Font('freesansbold.ttf', 32)
            text1 = font1.render('Which letter is this?', True, 'black', 'white')
            text1_rect = text1.get_rect()
            text1_rect.center = (RES[0]//2, 50)
            self.screen.blit(text1, text1_rect)

            self.game_state = 1

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.game_state == 0:
                        self.game_state = 2
                    elif self.game_state == 1:
                        self.game_state = 2

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()







