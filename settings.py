import pygame as pg
from images import *
pg.init()

# game settings
RES = WIDTH, HEIGHT = 1000, 600
FPS = 60

# draw level
question_font_1 = pg.font.Font('freesansbold.ttf', 44)
question_font_2 = pg.font.Font('freesansbold.ttf', 34)
question_font_3 = pg.font.Font('freesansbold.ttf', 54)


level_0_text_1 = question_font_1.render('The uppercase symbol for...', True, 'black', 'white')
level_0_text_2 = question_font_2.render('is...', True, 'black', 'white')

level_1_text_1 = question_font_1.render('The lowercase symbol for...', True, 'black', 'white')
level_1_text_2 = question_font_2.render('is...', True, 'black', 'white')

level_2_text_1 = question_font_1.render('Which letter is this?', True, 'black', 'white')
level_2_text_2 = question_font_2.render('is...', True, 'black', 'white')

level_0_text_1_rect = level_0_text_1.get_rect()
level_0_text_1_rect.center = (RES[0]//2, (RES[1] // 7) * 1)
level_0_text_2_rect = level_0_text_2.get_rect()
level_0_text_2_rect.center = (RES[0]//2, RES[1] // 2)

level_1_text_1_rect = level_1_text_1.get_rect()
level_1_text_1_rect.center = (RES[0]//2, (RES[1] // 7) * 1)
level_1_text_2_rect = level_1_text_2.get_rect()
level_1_text_2_rect.center = (RES[0]//2, RES[1] // 2)

level_2_text_1_rect = level_2_text_1.get_rect()
level_2_text_1_rect.center = (RES[0]//2, (RES[1] // 7) * 1)
level_2_text_2_rect = level_2_text_2.get_rect()
level_2_text_2_rect.center = (RES[0]//2, RES[1] // 2)

# draw answers
ans_font = pg.font.Font('freesansbold.ttf', 40)
font_buttons = pg.font.Font('freesansbold.ttf', 40)
font_selected_ans = pg.font.Font('freesansbold.ttf', 36)
text_selected_ans = font_selected_ans.render('You selected:', True, 'black', 'white')
text_selected_ans_rect = text_selected_ans.get_rect()
text_selected_ans_rect.center = (RES[0] // 2 - 100, 400)

# draw correct answer
font_correct_hdr = pg.font.Font('freesansbold.ttf', 46)
text_correct_hdr = font_correct_hdr.render('The correct answer is:', True, 'black', 'white')
text_correct_hdr_rect = text_correct_hdr.get_rect()
text_correct_hdr_rect.center = (RES[0]//2, 100)

font_correct_ans = pg.font.Font('freesansbold.ttf', 36)

text_compliment = font_selected_ans.render('Well done!', True, 'black', 'white')
text_compliment_rect = text_compliment.get_rect()
text_compliment_rect.center = (RES[0] // 2 - 100, 500)

# draw wrong answer
font_wrong_hdr = pg.font.Font('freesansbold.ttf', 46)
text_wrong_hdr = font_wrong_hdr.render('Wrong answer :( try again', True, 'black', 'white')
text_wrong_hdr_rect = text_wrong_hdr.get_rect()
text_wrong_hdr_rect.center = (RES[0]//2, 100)

#font_wrong_ans = pg.font.Font('freesansbold.ttf', 36)

# draw start screen
font_start = pg.font.Font('pythia.ttf', 60)
button_font = pg.font.Font('pythia.ttf', 40)

text_start_1 = font_start.render('GREEK', True, 'black', 'white')
text_start_1_rect = text_start_1.get_rect()
text_start_1_rect.center = (RES[0]//2, RES[1]//8)

text_start_2 = font_start.render('ALPHABET', True, 'black', 'white')
text_start_2_rect = text_start_2.get_rect()
text_start_2_rect.center = (RES[0]//2, RES[1]//8 + 100)

text_start_3 = font_start.render('TRAINER', True, 'black', 'white')
text_start_3_rect = text_start_3.get_rect()
text_start_3_rect.center = (RES[0]//2, RES[1]//8 + 200)

text_start_button = button_font.render('START', True, 'black', 'white')
text_start_button_rect = text_start_button.get_rect()
text_start_button_rect.center = (RES[0]//2, (RES[1]//3 * 2))

text_score_button = button_font.render('SCORE', True, 'black', 'white')
text_score_button_rect = text_score_button.get_rect()
text_score_button_rect.center = (RES[0]//2, ((RES[1]//3) * 2) + 60)

text_exit_button = button_font.render('EXIT', True, 'black', 'white')
text_exit_button_rect = text_exit_button.get_rect()
text_exit_button_rect.center = (RES[0]//2, (RES[1]//3 * 2) + 120)

start_buttons = [text_start_button, text_score_button, text_exit_button]

# draw
font1 = pg.font.Font('freesansbold.ttf', 52)



