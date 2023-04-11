import pygame as pg
from images import *
pg.init()

# game settings
RES = WIDTH, HEIGHT = 1000, 600
FPS = 60

# draw question
question_font = pg.font.Font('freesansbold.ttf', 64)

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

# draw
font_start = pg.font.Font('pythia.ttf', 60)

text_start_1 = font_start.render('GREEK', True, 'black', 'white')
text_start_1_rect = text_start_1.get_rect()
text_start_1_rect.center = (RES[0]//2, RES[1]//8)

text_start_2 = font_start.render('ALPHABET', True, 'black', 'white')
text_start_2_rect = text_start_2.get_rect()
text_start_2_rect.center = (RES[0]//2, RES[1]//8 + 100)

text_start_3 = font_start.render('TRAINER', True, 'black', 'white')
text_start_3_rect = text_start_3.get_rect()
text_start_3_rect.center = (RES[0]//2, RES[1]//8 + 200)

font1 = pg.font.Font('freesansbold.ttf', 52)
text1 = font1.render('Which letter is this?', True, 'black', 'white')
text1_rect = text1.get_rect()
text1_rect.center = (RES[0]//2, (RES[1] // 7) * 1)


