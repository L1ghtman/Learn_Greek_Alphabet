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
        self.answer_pair = []   # [render, rect, is_correct, text]

        self.state_3_buttons = []
        self.state_4_buttons = []

        self.rnd = 0

        self.selected = 0
        self.correct = 0

        self.prev_round = 0

        """
        levels:
        level == 0 => draw lowercase symbol or name, ask for uppercase symbol
        level == 1 => draw uppercase symbol or name, ask for lowercase symbol
        level == 2 => draw symbol (lowercase or uppercase), ask for name
        """
        self.level = 2

    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw_answers(self, i, lvl):
        self.answer_map = []
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        indices.remove(i)
        random.shuffle(indices)

        answers = [indices[0], indices[1], indices[2], indices[3], i]
        self.prev_round = answers
        random.shuffle(answers)

        correct_ans_index = answers.index(i)

        for a in range(0, 5):
            self.answer_pair = [0, 0, 0, 0]
            if lvl == 2:
                self.answer_pair[0] = ans_font.render(alphabet[answers[a]][lvl], True, 'black', 'white')
            else:
                self.answer_pair[0] = alphabet[answers[a]][lvl]
            self.answer_pair[1] = self.answer_pair[0].get_rect()
            self.answer_pair[3] = alphabet[answers[a]][lvl]

            if a == correct_ans_index:
                self.answer_pair[2] = 1
                self.correct = self.answer_pair

            self.answer_pair[1].center = ((RES[0] // 6) * (a + 1), (RES[1] // 4) * 3)
            self.answer_map.append(self.answer_pair)
            self.screen.blit(self.answer_map[a][0], self.answer_map[a][1])

    def draw_correct_answer(self):
        self.screen.fill('black')
        button_pair = [0, 0]

        text_correct_ans = font_correct_ans.render(alphabet[self.rnd][2], True, 'black', 'white')
        text_correct_ans_rect = text_correct_ans.get_rect()
        text_correct_ans_rect.center = (RES[0]//2, 200)

        selected = font_selected_ans.render(self.selected, True, 'black', 'green')
        selected_rect = selected.get_rect()
        selected_rect.center = (RES[0]//2 + 100, 400)

        button_pair[0] = font_buttons.render('NEXT', True, 'black', 'white')
        button_pair[1] = button_pair[0].get_rect()
        button_pair[1].center = (RES[0]//2 + 100, 500)

        self.state_3_buttons.append(button_pair)

        self.screen.blit(text_correct_hdr, text_correct_hdr_rect)
        self.screen.blit(text_correct_ans, text_correct_ans_rect)
        self.screen.blit(text_selected_ans, text_selected_ans_rect)
        self.screen.blit(selected, selected_rect)
        self.screen.blit(text_compliment, text_compliment_rect)
        self.screen.blit(self.state_3_buttons[0][0], self.state_3_buttons[0][1])

    def draw_wrong_answer(self):
        self.screen.fill('black')
        button_pair = [0, 0]

        selected = font_selected_ans.render(self.selected, True, 'black', 'red')
        selected_rect = selected.get_rect()
        selected_rect.center = (RES[0] // 2 + 100, 400)

        button_pair[0] = font_buttons.render('RETRY', True, 'black', 'white')
        button_pair[1] = button_pair[0].get_rect()
        button_pair[1].center = (RES[0]//2, 500)

        self.state_4_buttons.append(button_pair)

        self.screen.blit(text_wrong_hdr, text_wrong_hdr_rect)
        self.screen.blit(text_selected_ans, text_selected_ans_rect)
        self.screen.blit(selected, selected_rect)
        self.screen.blit(self.state_4_buttons[0][0], self.state_4_buttons[0][1])

    def draw_letter(self, i, lvl):
        j = random.randrange(0, 23) % 2
        print(j)
        k = random.randrange(0, 23) % 2
        print(k)
        match lvl:
            case 0:
                if k == 0:
                    letter_rect = alphabet[i][1].get_rect()
                    letter_rect.center = (RES[0] // 2, 200)
                    self.screen.blit(alphabet[i][1], letter_rect)
                else:
                    letter = ans_font.render(alphabet[i][2], True, 'black', 'white')
                    letter_rect = letter.get_rect()
                    letter_rect.center = (RES[0] // 2, 200)
                    self.screen.blit(letter, letter_rect)
            case 1:
                if k == 0:
                    letter_rect = alphabet[i][0].get_rect()
                    letter_rect.center = (RES[0] // 2, 200)
                    self.screen.blit(alphabet[i][0], letter_rect)
                else:
                    letter = ans_font.render(alphabet[i][2], True, 'black', 'white')
                    letter_rect = letter.get_rect()
                    letter_rect.center = (RES[0] // 2, 200)
                    self.screen.blit(letter, letter_rect)
            case 2:
                letter_rect = alphabet[i][j].get_rect()
                letter_rect.center = (RES[0] // 2, 200)
                self.screen.blit(alphabet[i][j], letter_rect)
            case _:
                pass

    def draw(self):
        lvl = random.randrange(0, 2)
        if self.game_state == 0:
            self.screen.blit(text_start, text_start_rect)

        elif self.game_state == 1:
            pass

        elif self.game_state == 2:
            self.screen.fill('black')
            self.rnd = random.randrange(0, 23)

            self.screen.blit(text1, text1_rect)

            i = self.rnd
            self.draw_letter(i, lvl)

            self.draw_answers(i, lvl)

            self.game_state = 1

        elif self.game_state == 3:
            self.draw_correct_answer()

        elif self.game_state == 4:
            self.draw_wrong_answer()

        elif self.game_state == 5:
            self.screen.fill('black')
            i = self.rnd

            self.draw_letter(i, lvl)

            self.screen.blit(text1, text1_rect)

            for a in range(0, 5):
                self.screen.blit(self.answer_map[a][0], self.answer_map[a][1])

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
                        is_pressed, button_rect = self.button_clicked([pair[1] for pair in self.answer_map])
                        if is_pressed == 1:
                            if self.is_correct_answer(button_rect) == 1:
                                self.game_state = 3
                            else:
                                self.game_state = 4
                        else:
                            self.game_state = 1
                    elif self.game_state == 3:
                        is_pressed, button_rect = self.button_clicked([pair[1] for pair in self.state_3_buttons])
                        if is_pressed == 1:
                            self.game_state = 2
                    elif self.game_state == 4:
                        is_pressed, button_rect = self.button_clicked([pair[1] for pair in self.state_4_buttons])
                        if is_pressed == 1:
                            self.game_state = 5

    def button_clicked(self, buttons):
        pos_x, pos_y = pg.mouse.get_pos()
        for button in buttons:
            if button[0] <= pos_x <= button[0] + button[2] and button[1] <= pos_y <= button[1] + button[3]:
                for pair in self.answer_map:
                    if pair[1] == button:
                        self.selected = pair[3]
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







