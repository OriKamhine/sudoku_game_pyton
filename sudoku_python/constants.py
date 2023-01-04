import pygame
pygame.init()



display = (800,800)
display = pygame.display.set_mode(display)
pygame.display.set_caption("SUDOKU - OK")
icon_img = pygame.image.load('icon_of_the_game.png')
pygame.display.set_icon(icon_img)
background_color = (21, 56, 53)


font_numbers = pygame.font.SysFont('Courier New', 80)
starting_font = pygame.font.SysFont('Courier New', 30)
specific_font = pygame.font.SysFont('Courier New', 60)


events = []
is_starting_screen = True
current_screen = 0


play_background_music_starting_screen = True
starting_music = pygame.mixer.Sound("start_music.mp3")


grid = None
easy_grid =     [[0, 5, 9, 0, 7, 0, 0, 8, 0],
                 [0, 1, 0, 5, 0, 4, 0, 9, 7],
                 [0, 0, 3, 0, 2, 0, 0, 1, 0],
                 [0, 0, 7, 2, 8, 0, 0, 0 ,9],
                 [0, 2, 6, 0, 0, 1, 3, 4, 0],
                 [5, 0, 0, 0, 6, 0, 8, 0, 0],
                 [0, 3, 0, 0, 5, 0, 7, 0, 0],
                 [9, 7, 0, 8, 0, 2, 0, 3, 0],
                 [0, 8, 0, 0, 4, 0, 9, 5, 0]]

mid_grid =      [[0, 0, 8, 3, 0, 0, 0, 9, 0],
                 [0, 0, 6, 0, 9, 0, 0, 4, 0],
                 [0, 2, 0, 0, 0, 6, 8, 0, 0],
                 [0, 0, 5, 0, 1, 0, 2, 6 ,0],
                 [4, 0, 0, 0, 3, 9, 0, 0, 8],
                 [0, 1, 9, 0, 8, 0, 3, 0, 0],
                 [0, 0, 1, 5, 0, 0, 0, 2, 0],
                 [0, 6, 0, 0, 7, 0, 1, 0, 0],
                 [0, 5, 0, 0, 0, 2, 9, 0, 0]]

hard_grid =     [[9, 0, 0, 0, 0, 7, 0, 0, 0],
                 [0, 0, 1, 3, 0, 0, 0, 4, 0],
                 [4, 0, 0, 0, 0, 2, 8, 0, 0],
                 [7, 0, 6, 0, 0, 0, 5, 0 ,0],
                 [0, 0, 5, 0, 0, 8, 3, 0, 0],
                 [0, 0, 9, 0, 7, 0, 1, 0, 6],
                 [0, 0, 4, 1, 0, 0, 0, 0, 9],
                 [0, 5, 0, 0, 0, 9, 2, 0, 0],
                 [0, 0, 0, 7, 0, 0, 0, 0, 3]]

list_levels = [easy_grid,mid_grid,hard_grid]


