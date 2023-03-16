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

        self.global_trigger = 0

        self.ans_1 = 0
        self.ans_2 = 0
        self.ans_3 = 0
        self.ans_4 = 0
        self.ans_5 = 0

        self.ans_1_rect = 0, 0, 0, 0
        self.ans_2_rect = 0, 0, 0, 0
        self.ans_3_rect = 0, 0, 0, 0
        self.ans_4_rect = 0, 0, 0, 0
        self.ans_5_rect = 0, 0, 0, 0

        self.i = 0

    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw_answers(self, i):
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        indices.remove(i)
        random.shuffle(indices)

        answers = [indices[0], indices[1], indices[2], indices[3], i]
        random.shuffle(answers)

        ans_font = pg.font.Font('freesansbold.ttf', 24)

        self.ans_1 = ans_font.render(alphabet[answers[0]][2], True, 'black', 'white')
        self.ans_1_rect = self.ans_1.get_rect()
        self.ans_1_rect.center = ((RES[0]//6), (RES[1]//4)*3)

        self.ans_2 = ans_font.render(alphabet[answers[1]][2], True, 'black', 'white')
        self.ans_2_rect = self.ans_2.get_rect()
        self.ans_2_rect.center = ((RES[0] // 6) * 2, (RES[1] // 4) * 3)

        self.ans_3 = ans_font.render(alphabet[answers[2]][2], True, 'black', 'white')
        self.ans_3_rect = self.ans_3.get_rect()
        self.ans_3_rect.center = ((RES[0] // 6) * 3, (RES[1] // 4) * 3)

        self.ans_4 = ans_font.render(alphabet[answers[3]][2], True, 'black', 'white')
        self.ans_4_rect = self.ans_4.get_rect()
        self.ans_4_rect.center = ((RES[0] // 6) * 4, (RES[1] // 4) * 3)

        self.ans_5 = ans_font.render(alphabet[answers[4]][2], True, 'black', 'white')
        self.ans_5_rect = self.ans_5.get_rect()
        self.ans_5_rect.center = ((RES[0] // 6) * 5, (RES[1] // 4) * 3)

        self.screen.blit(self.ans_1, self.ans_1_rect)
        self.screen.blit(self.ans_2, self.ans_2_rect)
        self.screen.blit(self.ans_3, self.ans_3_rect)
        self.screen.blit(self.ans_4, self.ans_4_rect)
        self.screen.blit(self.ans_5, self.ans_5_rect)

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

            letter_rect = alphabet[i][(i % 2)].get_rect()
            letter_rect.center = (RES[0]//2, 200)

            self.screen.blit(alphabet[i][(i % 2)], letter_rect)

            font1 = pg.font.Font('freesansbold.ttf', 32)
            text1 = font1.render('Which letter is this?', True, 'black', 'white')
            text1_rect = text1.get_rect()
            text1_rect.center = (RES[0]//2, 50)
            self.screen.blit(text1, text1_rect)

            self.draw_answers(i)

            self.game_state = 1

        if self.game_state == 3:
            self.screen.fill('green')

        # if self.global_trigger == 1:
            # pg.draw.rect(self.screen, 'green', self.ans_5_rect)

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

                        is_pressed, mouse_x, mouse_y = self.button_clicked([self.ans_1_rect, self.ans_2_rect, self.ans_3_rect,
                                                                  self.ans_4_rect, self.ans_5_rect])
                        if is_pressed == 1:
                            self.global_trigger = 1
                            self.game_state = 3

    def button_clicked(self, buttons):
        pos_x, pos_y = pg.mouse.get_pos()
        for button in buttons:
            if button[0] <= pos_x <= button[0] + button[2] and button[1] <= pos_y <= button[1] + button[3]:
                return 1, pos_x, pos_y
        return 0, pos_x, pos_y


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()







