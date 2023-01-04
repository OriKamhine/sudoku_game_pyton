import math
import time

import logical
from constants import *
import pygame
pygame.init()
from pygame import mixer


def starting_screen(): #The function of the starting screen
    global main_music_channel, play_background_music_starting_screen, grid
    main_music_channel = mixer.Channel(0)  # The channel of the music is 0, i create a channel because I have a variety of music

    background = pygame.image.load("the_real_one.png") #The image of the starting screen
    display.blit(background, (0, 0)) #Print the image background on the screen in place 0,0

    text_to_play = specific_font.render("Play", True, (255,255,255)) #Print the text on the screen
    text_rules = specific_font.render("Rules", True, (255,255,255)) #Print the text on the screen

    text_rules_rect = text_rules.get_rect() #Get the rectangle object and then he's getting its width property to calculate the position
    text_rules_rect.midbottom = (display.get_width() // 2, display.get_height()) #Midbottom because it's literally the midbottom, and the calculation
    text_to_play_rect = text_to_play.get_rect() #Get the rectangle object and then he's getting its width property to calculate the position
    text_to_play_rect.midbottom = (display.get_width() // 2, text_rules_rect.y) #Midbottom because it's literally the midbottom, and the calculation
    display.blit(text_to_play, text_to_play_rect) #Print the text on the screen
    display.blit(text_rules, text_rules_rect) #Print the text on the screen

    if any ([event.type == pygame.MOUSEBUTTONUP for event in events]): #If i wouldn't use the any function, the mouse button up didn't work
        pos = pygame.mouse.get_pos() #Function that getting the pos
        if text_to_play_rect.collidepoint(pos): #The crash between the mouse and the pos
            main_bg_music= mixer.Sound("background_music.mp3") #The music
            main_music_channel.set_volume(0.2) #The volume of the music
            main_music_channel.play(main_bg_music, loops=-1) #Makes the music to be infinity
            return 0 #Returns 0 because all the thing in "game" function
        if text_rules_rect.collidepoint(pos): #The crash between the mouse and the pos
            return 2 #Returns 2 because all the thing in "game" function
    pygame.display.flip() #Updates all
    return 3


def rules(): #The function of the rules
    global current_screen, is_starting_screen  # Make the variable events to be global in the project
    display.fill(background_color) #Fill the screen with the color of the background

    rule1_title = font_numbers.render("Rule 1: ", True, (255,255,255)) #Some text
    rule1_a = starting_font.render("Each row and column contains numbers 1 - 9,", True, (255,255,255)) #Some text
    rule1_b = starting_font.render("without repetitions the placement order", True, (255,255,255)) #Some text
    rule1_c = starting_font.render("of the digits, is irrelevant.", True, (255,255,255)) #Some text
    rule2_title  = font_numbers.render("Rule 2: ", True, (255,255,255))#Some text
    rule2_a = starting_font.render("A regular 9 x 9 grid is divided into 9,", True, (255,255,255)) #Some text
    rule2_b = starting_font.render("blocks of 3 x 3, also known as nonets.",True, (255,255,255)) #Some text
    rule2_c = starting_font.render("Numbers 1 - 9 can only occur once per net.", True, (255,255,255)) #Some text
    picture_rules = pygame.image.load("have_fun_image.png") #Load an image

    picture_rules = pygame.transform.scale(picture_rules, (300,350)) #Scale the image
    rect_back_to_menu = pygame.Rect(320, 585, 260, 60,)# To create the press, for the rectangle which actually do something when i press on him
    pygame.draw.rect(display, (255,255,255), rect_back_to_menu, 2) #Drawing the rectangle
    text_back_to_menu = starting_font.render("back to menu", True, (255,255,255)) #Some text in the rectangle

    event = pygame.event.poll() #Get a single event from the queue
    if event.type == pygame.MOUSEBUTTONUP: # (1) 5 lines which are creates the possibility for the rectangle to do something
        pos = pygame.mouse.get_pos() # (2)
        if rect_back_to_menu.collidepoint(pos): # (3)
            current_screen = 3 # (4)
            is_starting_screen = True # (5)

    display.blit(rule1_title,(10, 0)) #Print on the screen
    display.blit(rule1_a, (10, 80)) #Print on the screen
    display.blit(rule1_b, (10, 120)) #Print on the screen
    display.blit(rule1_c, (10, 160)) #Print on the screen
    display.blit(rule2_title, (10, 250)) #Print on the screen
    display.blit(rule2_a, (10, 330)) #Print on the screen
    display.blit(rule2_b,(10, 370)) #Print on the screen
    display.blit(rule2_c,(10, 410)) #Print on the screen
    display.blit(picture_rules,(0, 450)) #Print on the screen
    display.blit(text_back_to_menu, (450 - text_back_to_menu.get_width() / 2, 600)) #Print on the screen


def levels():
    display.fill((0,0,0))
    levels_picture = pygame.image.load("levels_real_real.png")
    display.blit(levels_picture, (0, 0))
    easy_button = pygame.Rect(350, 310, 105, 40)
    mid_button = pygame.Rect(330, 380, 145, 40)
    hard_button = pygame.Rect(350, 450, 105, 40)
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        if easy_button.collidepoint(pos):
            return 0 #easy
        if mid_button.collidepoint(pos):
            return 1 #mid
        if hard_button.collidepoint(pos):
            return 2 #hard
    if event.type == pygame.QUIT:
        quit()


def draw(first_iteration, second_iteration, third_iteration): #Function of the grid
    display.fill(background_color) #Fill screen    x  y  width height thickness
    pygame.draw.rect(display, (0,0,0), pygame.Rect(15, 15, 770, 770), 15) #Make the frame of the grid

    while (first_iteration * 85.55) < 770: #there are 8 lines, the margin is 770, 770 : 9 = 85.55
        pygame.draw.line(display, (0,0,0), ((first_iteration * 85.55) + 15, 15), ((first_iteration * 85.55) + 15, 785), 5) #Columns
        pygame.draw.line(display, (0,0,0), (15, (first_iteration * 85.55) + 15), (785, (first_iteration * 85.55) + 15), 5) #Rows
        first_iteration += 1 #while loop (iteration)

    while(second_iteration * 256.66) < 770: #To emphasize the columns, 770 : 3 = 256.66
        pygame.draw.line(display, (0, 0, 0), ((second_iteration * 256.66) + 15, 15), ((second_iteration * 256.66) + 15, 785),15) #Columns
        second_iteration += 1  #while loop (iteration)

    while(third_iteration * 256.66) < 770: #To emphasize the columns, 770 : 3 = 256.66
        pygame.draw.line(display, (0, 0, 0), (15, (third_iteration * 256.66) + 15), (785, (third_iteration * 256.66) + 15), 15) #Rows
        third_iteration += 1  #while loop (iteration)


def draw_numbers(): #Draw all the numbers in the beginning
    for column in range(len(logical.grid)): #For loop
        for row in range(len(logical.grid[column])): #Inside of for loop, i and j - they are grid box number, horizontal and vertical
            if 0 < logical.grid[column][row].value: #Check if value is a valid number,if the number between 1 - 9 put it on the screen
                color = (122, 133, 125) #Color changes if the location can be typed in
                if not logical.grid[column][row].is_taken: #If location can be typed in, in other word checks the cell and checks where is not the numbers that have already have been given
                    color = (255, 255, 255) #Color of the numbers that have already given
                value_number = font_numbers.render(str(logical.grid[column][row].value), True, color) #The string version of the grid, and the others - true
                display.blit(value_number, ((row + 1) * 85 - 50, (column + 1) * 85 - 65)) #Actually write on the screen, j and i start at 0 so we need to + 1


def insert_numbers(): #Insert numbers by the user
    global main_music_channel
    pressed_key = False  # For the while loop
    while not pressed_key: #While loop
        pos = pygame.mouse.get_pos() #Variable of the function position in python
        global events #Make the variable events to be global in the project
        events = pygame.event.get() #Save the event from running over
        for event in events: #For loop
            if event.type == pygame.QUIT: #If the player is quitting - exit
                quit() #Exits and closes the program
            elif event.type == pygame.KEYDOWN: #Pressed by the mouse button
                key = event.key #Variable
                row = math.floor((pos[0] - 15) / 85)  # Divided by 85 like in draw_numbers function, subtracted by 15 because this is the y and the x like in function draw that drawing the grid in  pos[0] = x and pos[1] = y
                column = math.floor((pos[1] - 15) / 85)  # index must be an integer, without the math.floor it would be float
                if pygame.K_1 <= key <= pygame.K_9:
                    if not logical.grid[column][row].is_taken and logical.checks(column, row, int (event.unicode)):
                        logical.grid[column][row].replace(int(event.unicode))
                        display.fill(background_color)
                        draw(first_iteration = 1, second_iteration = 1, third_iteration = 1)
                        draw_numbers()
                        pressed_key = True
                    else:
                        error_sound = mixer.Sound("erro.mp3")
                        main_music_channel.set_volume(0.7)
                        error_sound.play()

                if key == pygame.K_BACKSPACE:
                    if not logical.grid[column][row].is_taken:
                        logical.grid[column][row].replace(0)
                        display.fill(background_color)
                        draw(first_iteration=1, second_iteration=1, third_iteration=1)
                        draw_numbers()
                        pygame.display.flip()
                    else:
                        error_sound = mixer.Sound("erro.mp3")
                        main_music_channel.set_volume(0.7)
                        error_sound.play()


def game():
    global event,events, is_starting_screen, current_screen, main_music_channel, play_background_music_starting_screen,running
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
    if is_starting_screen:
        current_screen = starting_screen()
        if play_background_music_starting_screen:
            main_music_channel.play(starting_music, loops=-1)
            play_background_music_starting_screen = False
        if current_screen < 3:
            is_starting_screen = False
    if current_screen == 0:
        level_index = levels()
        if level_index == 0 or level_index == 1 or level_index == 2:
            current_screen = 1
            logical.generate_grid(level_index)
    if current_screen == 1:
        draw(first_iteration = 1, second_iteration = 1, third_iteration = 1)
        draw_numbers()
        pygame.display.flip()
        insert_numbers()
    elif current_screen == 2:
        rules()
    if logical.check_win():
        main_music_channel.stop()
        win_picture = pygame.image.load("win.png")
        win_picture = pygame.transform.scale(win_picture, (800, 800))
        display.blit(win_picture, (0,0))
        win_sound = mixer.Sound("win_sound.mp3")
        main_music_channel.set_volume(0.9)
        win_sound.play()
        pygame.display.flip()
        time.sleep(3)
        running = False
    pygame.display.flip()

running = True #Make a variable for the loop
while running: #Make a while loop
    game()