import pygame as pg
import matplotlib.pyplot as plt
import os
import sys
import random

from images import *
from settings import *

# general
# TODO: make sure letters dont repeat in a round
# TODO: add high score
# TODO: add exit button to every screen
# TODO: add lives / game over screen
# TODO: add sound effects
# TODO: add music
# TODO: add game modes (time, lives, spoken etc)
# TODO: increase probability of letters that weren't guessed correctly

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

        # for logging
        self.dist = [0] * 24

        self.game_state = 0

        self.answer_map = []
        self.answer_pair = []   # [render, rect, is_correct, text, frame]

        self.state_0_buttons = []
        self.state_1_buttons = []
        self.state_3_buttons = []
        self.state_4_buttons = []

        self.active_state = [0, 0, 0, 0, 0, 0]  # track if a game state is already active in order to be more efficient

        self.rnd = 0

        self.selected = []
        self.correct = 0

        self.prev_round = []
        self.is_retry = 0
        self.retry_pos = [0, 0]

        self.score = 0
        self.streak = 0
        self.lives = 3

        self.player_name = ''
        self.name_entered = False
        self.input_active = False

        """
        levels:
        level == 0 =>, draw lowercase symbol or name ask for uppercase symbol
        level == 1 => draw uppercase symbol or name, ask for lowercase symbol
        level == 2 => draw symbol (lowercase or uppercase), ask for name
        """
        self.level = 0

    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw_answers(self, i, lvl):
        self.answer_map = []

        if self.is_retry == 0:
            indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
            indices.remove(i)
            random.shuffle(indices)

            answers = [indices[0], indices[1], indices[2], indices[3], i]
            self.prev_round = answers
            random.shuffle(answers)

        answers = self.prev_round

        correct_ans_index = answers.index(i)

        for a in range(0, 5):
            self.answer_pair = [0, 0, 0, 0, 0]
            if lvl == 2:
                self.answer_pair[0] = ans_font.render(alphabet[answers[a]][2], True, 'black', 'white')
            else:
                self.answer_pair[0] = alphabet[answers[a]][lvl]
            self.answer_pair[1] = self.answer_pair[0].get_rect()
            self.answer_pair[3] = alphabet[answers[a]][2]
            self.answer_pair[1].center = ((((RES[0] + 100) // 6) * (a + 1)) - 50, (RES[1] // 16) * 13)

            self.answer_pair[4] = self.make_frame(self.answer_pair[1], 159, 176)

            if a == correct_ans_index:
                self.answer_pair[2] = 1
                self.correct = self.answer_pair

            self.answer_map.append(self.answer_pair)

            pg.draw.rect(self.screen, 'black', self.answer_pair[4], 2)

            self.screen.blit(self.answer_map[a][0], self.answer_map[a][1])

    def draw_correct_answer(self):
        self.active_state = [0, 0, 0, 1, 0, 0]
        self.state_3_buttons = []
        self.screen.fill('white')
        self.score = self.score + 1
        self.streak = self.streak + 1
        button_pair = [0, 0, 0]

        self.draw_lives(self.lives)

        if self.level == 0 or self.level == 1:
            image_sel_rect = self.selected[1]
            image_sel_rect.center = (RES[0] // 2, RES[1] // 4)
            self.screen.blit(self.selected[0], image_sel_rect)
        elif self.level == 2:
            text_correct = font_correct_ans.render(self.selected[3], True, 'black', 'white')
            text_correct_rect = text_correct.get_rect()
            text_correct_rect.center = (RES[0] // 2, RES[1] // 4)
            self.screen.blit(text_correct, text_correct_rect)

        # create 'next' button
        button_pair[0] = font_buttons.render('NEXT', True, 'black', 'white')
        button_pair[1] = button_pair[0].get_rect()
        button_pair[1].center = (RES[0] // 2, 500)
        button_pair[2] = self.make_frame(button_pair[1], 120, 50)

        # add buttons to list that will be used in check_events()
        self.state_3_buttons.append(button_pair)

        # draw score
        self.draw_score()

        # draw additional text
        self.screen.blit(text_correct_ans, text_cor_ans_rect)
        self.screen.blit(text_well_done, text_well_done_rect)

        # draw button text and frame
        self.screen.blit(self.state_3_buttons[0][0], self.state_3_buttons[0][1])
        pg.draw.rect(self.screen, 'black', self.state_3_buttons[0][2], 2)

    def draw_wrong_answer(self):
        self.active_state = [0, 0, 0, 0, 1, 0]
        self.state_4_buttons = []
        self.screen.fill('white')
        self.streak = 0
        button_pair = [0, 0, 0]

        self.draw_lives(self.lives)

        if self.level == 0 or self.level == 1:
            image_sel_rect = self.selected[1]
            image_sel_rect.center = (RES[0] // 2, RES[1] // 4)
            self.screen.blit(self.selected[0], image_sel_rect)
        elif self.level == 2:
            text_wrong = font_wrong_ans.render(self.selected[3], True, 'black', 'white')
            text_wrong_rect = text_wrong.get_rect()
            text_wrong_rect.center = (RES[0] // 2,  RES[1] // 4)
            self.screen.blit(text_wrong, text_wrong_rect)

        button_pair[0] = font_buttons.render('RETRY', True, 'black', 'white')
        button_pair[1] = button_pair[0].get_rect()
        button_pair[1].center = (RES[0] // 2, 500)
        button_pair[2] = self.make_frame(button_pair[1], 150, 50)

        self.state_4_buttons.append(button_pair)

        # draw score
        self.draw_score()

        self.screen.blit(text_wrong_hdr, text_wrong_hdr_rect)
        self.screen.blit(text_wrong_ans, text_wrong_ans_rect)
        self.screen.blit(self.state_4_buttons[0][0], self.state_4_buttons[0][1])
        pg.draw.rect(self.screen, 'black', self.state_4_buttons[0][2], 2)

    def draw_level(self, i, lvl):

        if self.is_retry == 1:
            k = self.retry_pos[0]
            j = self.retry_pos[1]
        else:
            k = random.randrange(0, 23) % 2
            j = random.randrange(0, 23) % 2
            self.retry_pos[0] = k
            self.retry_pos[1] = j
        match lvl:
            case 0:
                self.screen.blit(level_0_text_1, level_0_text_1_rect)
                if k == 0:
                    letter_rect = alphabet[i][1].get_rect()
                    letter_rect.center = (RES[0] // 2, (RES[1] // 6) * 2)
                    self.screen.blit(alphabet[i][1], letter_rect)
                else:
                    letter = ans_font.render(alphabet[i][2], True, 'black', 'white')
                    letter_rect = letter.get_rect()
                    letter_rect.center = (RES[0] // 2, (RES[1] // 6) * 2)
                    self.screen.blit(letter, letter_rect)

                self.screen.blit(level_0_text_2, level_0_text_2_rect)

            case 1:
                temp = pg.Rect(0, 0, 159, 176)
                temp.center = (RES[0] // 2, (RES[1] // 6) * 2)

                #pg.draw.rect(self.screen, 'green', temp)
                self.screen.blit(level_1_text_1, level_1_text_1_rect)
                if k == 0:
                    letter_rect = alphabet[i][0].get_rect()
                    letter_rect.center = (RES[0] // 2, (RES[1] // 6) * 2)
                    self.screen.blit(alphabet[i][0], letter_rect)
                else:
                    letter = question_font_3.render(alphabet[i][2], True, 'black', 'white')
                    letter_rect = letter.get_rect()
                    letter_rect.center = (RES[0] // 2, (RES[1] // 6) * 2)
                    self.screen.blit(letter, letter_rect)

                self.screen.blit(level_1_text_2, level_1_text_2_rect)

            case 2:
                self.screen.blit(level_2_text_1, level_2_text_1_rect)
                letter_rect = alphabet[i][j].get_rect()
                letter_rect.center = (RES[0] // 2, (RES[1] // 6) * 2)    # (RES[0] // 2, ((RES[1] // 5) * 2) - 50)
                self.screen.blit(alphabet[i][j], letter_rect)
            case _:
                pass

    def draw_score(self):
        # set score and streak text
        text_score = font_score.render('Score: ' + str(self.score), True, 'black', 'white')
        text_streak = font_score.render('Streak: ' + str(self.streak), True, 'black', 'white')

        # set location of score and streak
        if self.game_state == 1:
            text_score_rect = text_score.get_rect()
            text_streak_rect = text_streak.get_rect()
            text_score_rect.center = (RES[0] // 2, RES[1] // 2 - 50)
            text_streak_rect.center = (RES[0] // 2, RES[1] // 2)
        else:
            text_score_rect = pg.Rect(0, 0, 100, 30)
            text_streak_rect = pg.Rect(0, 30, 100, 30)

        # draw score and streak
        self.screen.blit(text_score, text_score_rect)
        self.screen.blit(text_streak, text_streak_rect)

    def draw_start_screen(self):
        self.active_state = [1, 0, 0, 0, 0, 0]
        self.screen.fill('white')

        start_frame = self.make_frame(text_start_button_rect, 200, 40)  # text_start_button_rect[2] <- use this to make the frame the same width as the button
        score_frame = self.make_frame(text_score_button_rect, 200, 40)  # text_score_button_rect[2]
        exit_frame = self.make_frame(text_exit_button_rect, 200, 40)  # text_exit_button_rect[2]

        self.state_0_buttons.append([text_start_button, text_start_button_rect, start_frame])
        self.state_0_buttons.append([text_score_button, text_score_button_rect, score_frame])
        self.state_0_buttons.append([text_exit_button, text_exit_button_rect, exit_frame])

        self.screen.blit(scaled_bicep_left, scaled_bicep_left_rect)
        self.screen.blit(scaled_bicep_right, scaled_bicep_right_rect)
        self.screen.blit(text_start_1, text_start_1_rect)
        self.screen.blit(text_start_2, text_start_2_rect)
        self.screen.blit(text_start_3, text_start_3_rect)
        self.screen.blit(text_start_button, text_start_button_rect)
        self.screen.blit(text_score_button, text_score_button_rect)
        self.screen.blit(text_exit_button, text_exit_button_rect)

        pg.draw.rect(self.screen, 'black', start_frame, 2)
        pg.draw.rect(self.screen, 'black', score_frame, 2)
        pg.draw.rect(self.screen, 'black', exit_frame, 2)

    def draw_game_screen(self):
        self.active_state = [0, 0, 1, 0, 0, 0]
        self.screen.fill('white')

        self.draw_score()
        self.draw_lives(self.lives)

        if self.is_retry == 0:
            self.rnd = random.randrange(0, 24)
            self.level = random.randrange(0, 3)

            self.dist[self.rnd] = self.dist[self.rnd] + 1

        self.draw_level(self.rnd, self.level)

        self.draw_answers(self.rnd, self.level)

        if self.is_retry == 1:
            self.is_retry = 0

    def draw_lives(self, lives):
        center_1 = (RES[0] - 25, 25)
        center_2 = (RES[0] - 75, 25)
        center_3 = (RES[0] - 125, 25)

        heart_rect_1 = heart.get_rect()
        heart_rect_2 = heart.get_rect()
        heart_rect_3 = heart.get_rect()

        heart_rect_1.center = center_1
        heart_rect_2.center = center_2
        heart_rect_3.center = center_3

        match lives:
            case 0:
                self.screen.blit(heart_dead, heart_rect_1)
                self.screen.blit(heart_dead, heart_rect_2)
                self.screen.blit(heart_dead, heart_rect_3)
            case 1:
                self.screen.blit(heart, heart_rect_1)
                self.screen.blit(heart_dead, heart_rect_2)
                self.screen.blit(heart_dead, heart_rect_3)
            case 2:
                self.screen.blit(heart, heart_rect_1)
                self.screen.blit(heart, heart_rect_2)
                self.screen.blit(heart_dead, heart_rect_3)
            case 3:
                self.screen.blit(heart, heart_rect_1)
                self.screen.blit(heart, heart_rect_2)
                self.screen.blit(heart, heart_rect_3)
            case _:
                pass

    def draw_game_over(self):
        self.active_state = [0, 1, 0, 0, 0, 0]
        self.screen.fill('white')
        self.lives = 3

        menu_frame = self.make_frame(text_menu_button_rect, text_menu_button_rect[2], 40)

        self.screen.blit(text_game_over, text_game_over_rect)

        self.draw_score()

        self.screen.blit(text_menu_button, text_menu_button_rect)

        pg.draw.rect(self.screen, 'black', menu_frame, 2)

        if not self.name_entered:
            self.draw_highscore()
        else:
            self.state_1_buttons.append([text_menu_button, text_menu_button_rect, menu_frame])

        #self.state_1_buttons.append([text_menu_button, text_menu_button_rect, menu_frame])


    def draw_highscore(self):
        pg.draw.rect(self.screen, 'white', pop_up_rect)
        pop_up_frame = self.make_frame(pop_up_rect, pop_up_rect.width, pop_up_rect.height)
        input_frame = self.make_frame(name_input_rect, name_input_rect.width, name_input_rect.height)
        pg.draw.rect(self.screen, 'black', pop_up_frame, 2)
        pg.draw.rect(self.screen, 'black', input_frame, 2)
        self.screen.blit(text_pop_up, text_pop_up_rect)

        # 'text_menu_button' and 'text_menu_button_rect' are not important and left as placeholders until I come up with some better solution
        self.state_1_buttons.append([text_menu_button, text_menu_button_rect, input_frame])

        input_font = pg.font.Font('pythia.ttf', 20)
        player_name_text = input_font.render(self.player_name, True, 'black', 'white')
        self.screen.blit(player_name_text, (input_frame.x+5, input_frame.y+5))

    def draw(self):

        if self.game_state == 0:
            if self.active_state[0]:
                pass
            else:
                self.draw_start_screen()

        elif self.game_state == 1:
            if self.active_state[1]:
                self.draw_game_over()
            else:
                self.draw_game_over()

        elif self.game_state == 2:
            if self.active_state[2]:
                pass
            else:
                self.draw_game_screen()

        elif self.game_state == 3:
            if self.active_state[3]:
                pass
            else:
                self.draw_correct_answer()

        elif self.game_state == 4:
            if self.active_state[4]:
                pass
            else:

                self.draw_wrong_answer()

    def add_to_highscore(self, name, score, streak):
        high_scores = open('highscores.txt', 'r')
        scores = high_scores.readlines()
        high_scores.close()
        scores.append(name + ',' + str(score) + ',' + str(streak) + '\n')
        scores.sort(key = lambda x: int(x.split(',')[1]), reverse=True)
        high_scores = open('highscores.txt', 'w')
        high_scores.writelines(scores)
        high_scores.close()

    def add_to_log(self):
        print(self.dist)
        log_list = []
        log = open('distribution_log.txt', 'r')
        log_lines = log.readline().split(',')
        log.close()
        if len(log_lines) > 1:
            for i in range(0, 24):
                self.dist[i] = self.dist[i] + int(log_lines[i])
                log_list.append(str(self.dist[i]))
        else:
            for i in range(0, 24):
                log_list.append(str(self.dist[i]))
        log = open('distribution_log.txt', 'w')
        print(log_list)
        log.write(','.join(log_list))
        log.close()

    def plot_distribution(self):
        log = open('distribution_log.txt', 'r')
        log_lines = [int(i) for i in log.readline().split(',')]
        log.close()

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        distribution = log_lines
        ax.bar(letters, distribution)
        plt.show()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.add_to_log()
                self.plot_distribution()
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.game_state == 0:
                        is_pressed, button_rect = self.button_clicked([pair[2] for pair in self.state_0_buttons])
                        if is_pressed == 1:
                            if button_rect == self.state_0_buttons[0][2]:
                                self.game_state = 2
                            elif button_rect == self.state_0_buttons[1][2]:
                                pass
                            elif button_rect == self.state_0_buttons[2][2]:
                                self.add_to_log()
                                self.plot_distribution()
                                pg.quit()
                                sys.exit()
                    elif self.game_state == 1:
                        is_pressed, button_rect = self.button_clicked([pair[2] for pair in self.state_1_buttons])
                        if is_pressed == 1:
                            if button_rect == self.state_1_buttons[0][2]:
                                self.input_active = True
                                #if button_rect == self.state_1_buttons[2][2]:
                                #self.game_state = 0
                    elif self.game_state == 2:
                        is_pressed, button_rect = self.button_clicked([pair[4] for pair in self.answer_map])
                        if is_pressed == 1:
                            if self.is_correct_answer(button_rect) == 1:
                                self.game_state = 3
                            else:
                                if self.lives == 1:
                                    self.game_state = 1
                                else:
                                    self.lives -= 1
                                    self.game_state = 4
                        else:
                            self.game_state = 2
                    elif self.game_state == 3:
                        is_pressed, button_rect = self.button_clicked([pair[2] for pair in self.state_3_buttons])
                        if is_pressed == 1:
                            self.game_state = 2
                    elif self.game_state == 4:
                        is_pressed, button_rect = self.button_clicked([pair[2] for pair in self.state_4_buttons])
                        if is_pressed == 1:
                            self.game_state = 2
                            self.is_retry = 1
            elif event.type == pg.KEYDOWN:
                if self.input_active:
                    if event.key == pg.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    else:
                        self.player_name += event.unicode

    def button_clicked(self, buttons):
        pos_x, pos_y = pg.mouse.get_pos()
        for button in buttons:
            if button[0] <= pos_x <= button[0] + button[2] and button[1] <= pos_y <= button[1] + button[3]:
                for pair in self.answer_map:
                    if pair[4] == button:
                        self.selected = pair
                return 1, button
        return 0, buttons[0]

    def is_correct_answer(self, button):
        for triple in self.answer_map:      # TODO: renaming required
            rect = triple[4]
            if rect == button and triple[2] == 1:
                return 1
        return 0

    def make_frame(self, rect, width, height):
        frame_x = rect[0] - 7
        frame_y = rect[1] - 7
        frame = pg.Rect(frame_x, frame_y, width + 14, height + 14)
        frame.center = rect.center
        return frame

    def run(self):
        self.add_to_highscore('test', 100, 10)
        self.add_to_highscore('test2', 200, 20)
        self.add_to_highscore('test3', 300, 30)
        self.add_to_highscore('test4', 400, 40)
        self.add_to_highscore('test5', 500, 50)
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()







