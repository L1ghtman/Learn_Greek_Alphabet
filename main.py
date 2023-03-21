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

        self.answer_map = []
        self.answer_pair = []

        self.state_3_buttons = []

        self.rnd = 0

        self.selected = 0
        self.correct = 0

    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw_answers(self, i):
        self.answer_map = []
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        indices.remove(i)
        random.shuffle(indices)

        answers = [indices[0], indices[1], indices[2], indices[3], i]
        random.shuffle(answers)

        correct_ans_index = answers.index(i)

        ans_font = pg.font.Font('freesansbold.ttf', 24)

        for a in range(0, 5):
            self.answer_pair = [0, 0, 0]
            self.answer_pair[0] = ans_font.render(alphabet[answers[a]][2], True, 'black', 'white')
            self.answer_pair[1] = self.answer_pair[0].get_rect()

            if a == correct_ans_index:
                self.answer_pair[2] = 1
                self.correct = self.answer_pair

            self.answer_pair[1].center = ((RES[0] // 6) * (a + 1), (RES[1] // 4) * 3)
            self.answer_map.append(self.answer_pair)
            self.screen.blit(self.answer_map[a][0], self.answer_map[a][1])

    def draw_correct_answer(self):
        self.screen.fill('black')
        self.state_3_buttons = [0, 0, 0]
        font_buttons = pg.font.Font('freesansbold.ttf', 40)

        font_correct_hdr = pg.font.Font('freesansbold.ttf', 46)
        text_correct_hdr = font_correct_hdr.render('The correct answer is:', True, 'black', 'white')
        text_correct_hdr_rect = text_correct_hdr.get_rect()
        text_correct_hdr_rect.center = (RES[0]//2, 100)

        font_correct_ans = pg.font.Font('freesansbold.ttf', 36)
        text_correct_ans = font_correct_ans.render(alphabet[self.rnd][2], True, 'black', 'white')
        text_correct_ans_rect = text_correct_ans.get_rect()
        text_correct_ans_rect.center = (RES[0]//2, 200)

        font_selected_ans = pg.font.Font('freesansbold.ttf', 36)
        text_selected_ans = font_selected_ans.render('You selected:', True, 'black', 'white')
        text_compliment = font_selected_ans.render('Well done!', True, 'black', 'white')
        text_selected_ans_rect = text_selected_ans.get_rect()
        text_compliment_rect = text_compliment.get_rect()
        text_selected_ans_rect.center = (RES[0]//2 - 100, 400)
        text_compliment_rect.center =(RES[0]//2 - 100, 500)

        self.selected[1].center = (RES[0]//2 + 100, 400)

        self.state_3_buttons[0] = font_buttons.render('NEXT', True, 'black', 'white')
        self.state_3_buttons[1] = self.state_3_buttons[0].get_rect()
        self.state_3_buttons[1].center = (RES[0]//2 + 100, 400)

        self.screen.blit(text_correct_hdr, text_correct_hdr_rect)
        self.screen.blit(text_correct_ans, text_correct_ans_rect)
        self.screen.blit(text_selected_ans, text_selected_ans_rect)
        self.screen.blit(self.selected[0], self.selected[1])
        self.screen.blit(self.state_3_buttons[0], self.state_3_buttons[1])

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
            self.rnd = random.randrange(0, 23, 1)
            i = self.rnd

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

        elif self.game_state == 3:
            self.draw_correct_answer()

        elif self.game_state == 4:
            self.screen.fill('red')
            baustelle = pg.image.load('sprites/baustelle.jpg')
            baustelle_rect = baustelle.get_rect()
            self.screen.blit(baustelle, baustelle_rect)

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
                        is_pressed, button_rect = self.button_clicked([pair[1] for pair in self.answer_map])
                        if is_pressed == 1:
                            if self.is_correct_answer(button_rect) == 1:
                                self.game_state = 3
                            else:
                                self.game_state = 4
                        else:
                            self.game_state = 2

    def button_clicked(self, buttons):
        pos_x, pos_y = pg.mouse.get_pos()
        for button in buttons:
            if button[0] <= pos_x <= button[0] + button[2] and button[1] <= pos_y <= button[1] + button[3]:
                for pair in self.answer_map:
                    if pair[1] == button:
                        self.selected = pair
                return 1, button
        return 0, buttons[0]

    def is_correct_answer(self, button):
        for triple in self.answer_map:
            rect = triple[1]
            if rect == button and triple[2] == 1:
                return 1
        return 0

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()







