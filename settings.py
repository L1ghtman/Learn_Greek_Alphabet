import pygame as pg
from images import *
pg.init()

# game settings
RES = WIDTH, HEIGHT = 1000, 600
FRAME_DIM = 159, 176
FPS = 60

# draw level
question_font_1 = pg.font.Font('freesansbold.ttf', 44)
question_font_2 = pg.font.Font('freesansbold.ttf', 34)
question_font_3 = pg.font.Font('freesansbold.ttf', 54)
font_score = pg.font.Font('freesansbold.ttf', 30)

level_0_text_1 = question_font_1.render('The uppercase symbol for...', True, 'black', 'white')
level_0_text_2 = question_font_2.render('is...', True, 'black', 'white')

level_1_text_1 = question_font_1.render('The lowercase symbol for...', True, 'black', 'white')
level_1_text_2 = question_font_2.render('is...', True, 'black', 'white')

level_2_text_1 = question_font_1.render('Which letter is this?', True, 'black', 'white')
level_2_text_2 = question_font_2.render('is...', True, 'black', 'white')

level_0_text_1_rect = level_0_text_1.get_rect()
level_0_text_1_rect.center = (RES[0]//2, (RES[1] // 9) * 1)
level_0_text_2_rect = level_0_text_2.get_rect()
level_0_text_2_rect.center = (RES[0]//2, (RES[1] // 9) * 5)

level_1_text_1_rect = level_1_text_1.get_rect()
level_1_text_1_rect.center = (RES[0]//2, (RES[1] // 9) * 1)
level_1_text_2_rect = level_1_text_2.get_rect()
level_1_text_2_rect.center = (RES[0]//2, (RES[1] // 9) * 5)

level_2_text_1_rect = level_2_text_1.get_rect()
level_2_text_1_rect.center = (RES[0]//2, (RES[1] // 7) * 1)
level_2_text_2_rect = level_2_text_2.get_rect()
level_2_text_2_rect.center = (RES[0]//2, RES[1] // 2)

# draw answers
ans_font = pg.font.Font('freesansbold.ttf', 40)
font_buttons = pg.font.Font('freesansbold.ttf', 40)

# draw correct answer
font_well_done = pg.font.Font('freesansbold.ttf', 46)
font_correct_ans = pg.font.Font('freesansbold.ttf', 36)

text_well_done = font_well_done.render('Well Done', True, 'black', 'white')
text_correct_ans = font_correct_ans.render('... is correct!', True, 'black', 'white')

text_well_done_rect = text_well_done.get_rect()
text_cor_ans_rect = text_correct_ans.get_rect()

text_well_done_rect.center = (RES[0]//2, RES[1]//2 + 100)
text_cor_ans_rect.center = (RES[0]//2, RES[1]//2)

# draw wrong answer
font_wrong_hdr = pg.font.Font('freesansbold.ttf', 46)
font_wrong_ans = pg.font.Font('freesansbold.ttf', 36)

text_wrong_hdr = font_wrong_hdr.render('Don\'t cry, try again! :)', True, 'black', 'white')
text_wrong_ans = font_wrong_ans.render('... is wrong :(', True, 'black', 'white')

text_wrong_hdr_rect = text_wrong_hdr.get_rect()
text_wrong_ans_rect = text_wrong_ans.get_rect()

text_wrong_hdr_rect.center = (RES[0]//2, RES[1]//2 + 100)
text_wrong_ans_rect.center = (RES[0]//2, RES[1]//2)

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

# draw game over screen
font_game_over = pg.font.Font('pythia.ttf', 60)
font_menu_button = pg.font.Font('freesansbold.ttf', 40)

text_game_over = font_game_over.render('GAME OVER', True, 'black', 'white')
text_menu_button = font_menu_button.render('MAIN MENU', True, 'black', 'white')

text_game_over_rect = text_game_over.get_rect()
text_menu_button_rect = text_menu_button.get_rect()

text_game_over_rect.center = (RES[0]//2, RES[1]//4)
text_menu_button_rect.center = (RES[0]//2, (RES[1]//4) * 3)

# draw highscore pop-up
font_pop_up = pg.font.Font('pythia.ttf', 30)
font_name_input = pg.font.Font(None, 30)
font_submit_button = pg.font.Font('pythia.ttf', 40)

text_pop_up = font_pop_up.render('You made it to the leaderboard!', True, 'black', 'white')
text_submit_button = font_submit_button.render('Submit', True, 'black', 'white')

pop_up_rect = pg.Rect(RES[0]//3, RES[1]//4, 2*(RES[0]//3), 4*(RES[1]//8))
text_pop_up_rect = text_pop_up.get_rect()
name_input_rect = pg.Rect(0, 0, 300, 35)
text_submit_button_rect = text_submit_button.get_rect()

pop_up_rect.center = (RES[0]//2, 5*(RES[1]//8))
text_pop_up_rect.center = (RES[0]//2, RES[1]//2)
name_input_rect.center = (RES[0]//2, 11*(RES[1]//16))
text_submit_button_rect.center = (RES[0]//2, 13*(RES[1]//16))

# draw leaderboard
font_leaderboard_title = pg.font.Font('pythia.ttf', 40)
font_entry = pg.font.Font('pythia.ttf', 20)
font_leaderboard_button = pg.font.Font('pythia.ttf', 30)

text_leaderboard_title = font_leaderboard_title.render('Leaderboard', True, 'black', 'white')
text_leaderboard_position = font_entry.render('Position', True, 'black', 'white')
text_leaderboard_name = font_entry.render('Name', True, 'black', 'white')
text_leaderboard_score = font_entry.render('Score', True, 'black', 'white')
text_leaderboard_streak = font_entry.render('Streak', True, 'black', 'white')
text_leaderboard_exit_button = font_leaderboard_button.render('Go back', True, 'black', 'white')
text_leaderboard_pos1 = font_entry.render('1', True, 'black', 'white')
text_leaderboard_pos2 = font_entry.render('2', True, 'black', 'white')
text_leaderboard_pos3 = font_entry.render('3', True, 'black', 'white')
text_leaderboard_pos4 = font_entry.render('4', True, 'black', 'white')
text_leaderboard_pos5 = font_entry.render('5', True, 'black', 'white')
text_leaderboard_pos6 = font_entry.render('6', True, 'black', 'white')
text_leaderboard_pos7 = font_entry.render('7', True, 'black', 'white')
text_leaderboard_pos8 = font_entry.render('8', True, 'black', 'white')
text_leaderboard_pos9 = font_entry.render('9', True, 'black', 'white')
text_leaderboard_pos10 = font_entry.render('10', True, 'black', 'white')

text_leaderboard_title_rect = text_leaderboard_title.get_rect()
text_leaderboard_position_rect = text_leaderboard_position.get_rect()
text_leaderboard_name_rect = text_leaderboard_name.get_rect()
text_leaderboard_score_rect = text_leaderboard_score.get_rect()
text_leaderboard_streak_rect = text_leaderboard_streak.get_rect()
text_leaderboard_exit_button_rect = text_leaderboard_exit_button.get_rect()
text_leaderboard_pos1_rect = text_leaderboard_pos1.get_rect()
text_leaderboard_pos2_rect = text_leaderboard_pos2.get_rect()
text_leaderboard_pos3_rect = text_leaderboard_pos3.get_rect()
text_leaderboard_pos4_rect = text_leaderboard_pos4.get_rect()
text_leaderboard_pos5_rect = text_leaderboard_pos5.get_rect()
text_leaderboard_pos6_rect = text_leaderboard_pos6.get_rect()
text_leaderboard_pos7_rect = text_leaderboard_pos7.get_rect()
text_leaderboard_pos8_rect = text_leaderboard_pos8.get_rect()
text_leaderboard_pos9_rect = text_leaderboard_pos9.get_rect()
text_leaderboard_pos10_rect = text_leaderboard_pos10.get_rect()

text_leaderboard_title_rect.center = (RES[0]//2, RES[1]//14)
text_leaderboard_position_rect.center = (1*(RES[0]//5), 2*(RES[1]//14))
text_leaderboard_name_rect.center = (2*(RES[0]//5), 2*(RES[1]//14))
text_leaderboard_score_rect.center = (3*(RES[0]//5), 2*(RES[1]//14))
text_leaderboard_streak_rect.center = (4*(RES[0]//5), 2*(RES[1]//14))
text_leaderboard_exit_button_rect.center = (RES[0]//2, 13*(RES[1]//14) + 10)
text_leaderboard_pos1_rect.center = (RES[0]//5, 3*(RES[1]//14))
text_leaderboard_pos2_rect.center = (RES[0]//5, 4*(RES[1]//14))
text_leaderboard_pos3_rect.center = (RES[0]//5, 5*(RES[1]//14))
text_leaderboard_pos4_rect.center = (RES[0]//5, 6*(RES[1]//14))
text_leaderboard_pos5_rect.center = (RES[0]//5, 7*(RES[1]//14))
text_leaderboard_pos6_rect.center = (RES[0]//5, 8*(RES[1]//14))
text_leaderboard_pos7_rect.center = (RES[0]//5, 9*(RES[1]//14))
text_leaderboard_pos8_rect.center = (RES[0]//5, 10*(RES[1]//14))
text_leaderboard_pos9_rect.center = (RES[0]//5, 11*(RES[1]//14))
text_leaderboard_pos10_rect.center = (RES[0]//5, 12*(RES[1]//14))

# draw
font1 = pg.font.Font('freesansbold.ttf', 52)



