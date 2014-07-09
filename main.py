import pygame, sys, random
from pygame.locals import *


#################CLASSES################
class Cell: 
    def __init__(self, color, (numx, numy), square):
        self.color = color
        self.x = numx
        self.y = numy
        self.square = square
        self.visited = False
        #Adjacent order   N   E   S   W
        self.adjacents = ["", "", "", ""]

    def __str__(self):
        return str(self.color) + '(' + str(self.x) + ', ' + str(self.y) + ')'

    def set_adjacent(self, cell, direction):
        if direction == 'N':
            self.adjacents[3] = cell
        elif direction == 'E':
            self.adjacents[2] = cell
        elif direction == 'S':
            self.adjacents[1] = cell
        elif direction == 'W':
            self.adjacents[0] = cell

    def visit(self):
        self.visited = True

    def unvisit(self):
        self.visited = False

    def is_visited(self):
        return self.visited

    #If this cell is out of bounds, its color shall be 0.
    def is_out_of_bounds(self):
        return self.color == 9

class Matrix:
    uniform_color_count = 0

    def __init__(self, n):
        self.array = [[0 for x in xrange(int(n))] for y in xrange(int(n))]
        self.length = n
        self.size = n * n
        # Create and fill matrix
        self._make_array(n)

    # Make squares and random colors for each. Put square in newly created Cell
    # Put new Cell into 2d array. Display the square with a randomly chosen 
    # color.
    def _make_array(self, n):
        random.seed()
        for x in range(0, n):
            for y in range(0, n):
                random_color = random.randint(0, 6)
                square = pygame.Rect(x * 20 + 40, y * 20 + 70, 20, 20)
                self.array[x][y] = Cell(random_color, (x, y), square)

    def get(self, x, y):
        return self.array[x][y]

    def __str__(self):
        string = ""
        for y in range(0, self.length):
            for x in range(0, self.length):
                string += str(self.array[x][y].color) + ' '
            if y < self.length - 1:
                string += '\n'
        return string

# Abstract class
class Screen:
    def update(self):
        raise NotImplementedError('Subclass must implemment abstract method')

# Concrete classes
class MenuScreen(Screen):
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.title = self.font.render('Color Flows', True, GREEN, BLUE)
        self.text_rect_obj = self.title.get_rect()
        self.text_rect_obj.center = (200, 50)

    def update(self):
        DISPLAYSURFACE.blit(self.title, self.text_rect_obj)

class PlayScreen(Screen):
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        # Create squares for palette_list
        for x in range(0, len(colors)):
            square = pygame.Rect(x * 50 + 10, 10, 40, 40)
            palette_list.append(square)
        # Create back-to-menu surface. 
        exit_to_menu_string = 'Back to menu'
        self.exit_to_menu_surf = self.font.render(exit_to_menu_string, True, RED,
                                                  BLACK)
        # Since the rectangle inherent inside exit_menu_surf cannot be altered,
        # a new rectangle is created from the get() function and used for the
        # positioning of btm surface.
        self.exit_rect = self.exit_to_menu_surf.get_rect()
        self.exit_rect.x = 30
        self.exit_rect.y = 330

    def update(self):
        # Render color palette
        for index, palette_square in enumerate(palette_list):            
            pygame.draw.rect(DISPLAYSURFACE, colors[index], palette_square)
        # Render color grid
        for x in range(0, matrix.length):
            for y in range(0, matrix.length):
                pygame.draw.rect(DISPLAYSURFACE, colors[matrix.get(x, y).color],
                                 matrix.get(x, y).square)
        # Render high score
        score_str = 'Score: ' + str(score)
        score_text = self.font.render(score_str, True, RED, BLACK)
        score_text_obj = score_text.get_rect()
        score_text_obj.center = (400, 150)
        DISPLAYSURFACE.blit(score_text, score_text_obj)
        # Render back-to-menu button (temporary)                
        DISPLAYSURFACE.blit(self.exit_to_menu_surf, self.exit_rect)


###########FUNCTIONS#######################
#Make and set adjacents
def set_adjacent_cells(matrix):
    for x in range(0, matrix.length):
        for y in range(0, matrix.length):
            cell = matrix.get(x, y)
            xw = x - 1
            xe = x + 1
            yn = y - 1
            ys = y + 1

            if yn < 0:
                cell.set_adjacent(Cell(9, (x, yn), ""), "N")
            else:
                cell.set_adjacent(matrix.get(x, yn), "N")

            if xe >= matrix.length:
                cell.set_adjacent(Cell(9, (xe, y), ""), "E")
            else: 
                cell.set_adjacent(matrix.get(xe, y), "E")

            if ys >= matrix.length:
                cell.set_adjacent(Cell(9, (x, ys), ""), "S")
            else:
                cell.set_adjacent(matrix.get(x, ys), "S")

            if xw < 0:
                cell.set_adjacent(Cell(9, (xw, y), ""), "W")
            else:
                cell.set_adjacent(matrix.get(xw, y), "W")

##Depth First Search
# Non-recursive implementation. unvisited_cells will be the stack that takes in 
# cells that are adjacent to the current cell. At each iteration of the while 
# loop, all consecutive cells on top of the stack that are already visited will 
# be removed. The next cell on top of the stack, hence, is unvisited. It will be
# set to "visited" and then all of its adjacent cells are added onto the stack. 
def traversal_algorithm1(cell, fill_color):
    visited_cell_count = 0
    total_cell_count = matrix.length * matrix.length
    cells_to_visit = [cell]
    visited_cells = [] #To unvisit after the loop

    while len(cells_to_visit) > 0 and visited_cell_count <= total_cell_count:    
        while True:
            if not cells_to_visit:
                break
            else:
                if cells_to_visit[-1].is_visited():
                    cells_to_visit.pop()
                else:
                    break
        if not cells_to_visit:
            break

        current_cell = cells_to_visit.pop()
        current_cell.visit()
        visited_cell_count += 1
        prev_color = current_cell.color
        current_cell.color = fill_color
        pygame.draw.rect(DISPLAYSURFACE, colors[fill_color], 
                         current_cell.square)
        visited_cells.append(current_cell)

        # counter = 0
        for adj_cell in current_cell.adjacents:
            if not adj_cell.is_out_of_bounds():
                if adj_cell.color == prev_color or adj_cell.color == fill_color:
                    cells_to_visit.append(adj_cell)

    matrix.uniform_color_count = len(visited_cells)
    for visited_cell in visited_cells:
        visited_cell.unvisit()



###############Main Script ####################
pygame.init()

# Set up window
DISPLAYSURFACE = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Color Flow')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BROWN = (120, 42, 70)
colors = [RED, GREEN, BLUE, PURPLE, YELLOW, ORANGE, BROWN]
#  0     1      2     3       4       5       6
DISPLAYSURFACE.fill(WHITE)

matrix = Matrix(12)
palette_list = []

score = 0
set_adjacent_cells(matrix)
pygame.display.update()
prev_color_number = matrix.get(0, 0).color
color_number = prev_color_number

menu_screen = MenuScreen()
play_screen = PlayScreen()
current_screen = play_screen
print ##########TEST AREA############

print ##########END TEST AREA###########

###### Main game loop
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            counter = 0
            # Establish changing color by using mouse clicked coordinates. 
            # Counter is the index used to locate color in color list.
            for square in palette_list:
                if square.collidepoint(mouse_x, mouse_y):
                    color_number = counter
                    break
                else:
                    counter += 1
            # If chosen color is not the same as before,        
            if color_number != prev_color_number:
                traversal_algorithm1(matrix.get(0, 0), int(color_number))
                score += 1
                prev_color_number = color_number
            
            # Todo: encapsulate into Screen object or another object            
            rectangle = current_screen.exit_rect
            if rectangle.collidepoint(mouse_x, mouse_y):
                DISPLAYSURFACE.fill(BLACK)
                current_screen = menu_screen

    current_screen.update()    
    pygame.display.update()

######## End loop ######
