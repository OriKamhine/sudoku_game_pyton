from number import Number
from constants import *

grid = [[Number(0)]]
def generate_grid(level_index):
    global grid
    grid = list_levels[level_index]
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            grid[column][row] = Number(grid[column][row])

def checks(column, row, input_user): #tells python to keep the process and drop a line
    return \
        all([loop_row.value != input_user  # Value isn't taken
             for loop_row in grid[column]]  #For each value horizontally
            ) \
        and \
        all([loop_column[row].value != input_user  #Value isn't taken
             for loop_column in grid]  #For each value vertically
            ) \
        and \
        all([area_cell.value != input_user  #Value isn't taken
                             for area_cell in [grid[loop_column][loop_row]  #For each grid item in placed grid
                                 for loop_column in range(len(grid))
                                   for loop_row in range(len(grid[loop_column]))  #Index in column loop_column , and because loop_column updates it will move to the the next column
                                        if loop_column // 3 == column // 3 and loop_row // 3 == row // 3]]  #If the grid item is in the value's 3x3 group
            )

def check_win():
    return all([row.value > 0 for column in grid for row in column])
