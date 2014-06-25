import pygame, sys, random
from pygame.locals import *

pygame.init()
 
# Set up window
DISPLAYSURFACE = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Color Flow')

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BROWN = (165, 42, 42)
colors = [RED, GREEN, BLUE, PURPLE, YELLOW, ORANGE, BROWN]
        #  0     1      2     3       4       5       6
DISPLAYSURFACE.fill(WHITE)
redrect = pygame.Rect(10, 20, 20, 20)
greenrect = pygame.Rect(30, 20, 20, 20)
bluerect = pygame.Rect(10, 40, 20, 20)
pygame.draw.rect(DISPLAYSURFACE, RED, redrect)
pygame.draw.rect(DISPLAYSURFACE, GREEN, greenrect)
pygame.draw.rect(DISPLAYSURFACE, BLUE, bluerect)






class Cell: 
    color = ""
    x = ""
    y = ""
    visited = ""
    adjacents = ""

    def __init__(self, color, (numx, numy)):
        self.color = color
        self.x = numx
        self.y = numy
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
        return self.color == 0

class Matrix:
    array = ""
    length = ""
    size = ""
    uniform_color_count = 0

    def __init__(self, n):
        self.array = [[0 for x in xrange(int(n))] for y in xrange(int(n))]
        self.length = n
        self.size = n * n
        # Create and fill matrix
        self._make_array(n)

    def _make_array(self, n):
        random.seed()
        for x in range(0, n):
            for y in range(0, n):
                random_color = random.randint(0, 6)
                self.array[x][y] = Cell(random_color, (x, y))
                rect = pygame.Rect(x * 20 + 10, y * 20 + 20, 20, 20)
                pygame.draw.rect(DISPLAYSURFACE, colors[random_color], rect)

    def get(self, x, y):
        return self.array[x][y]

    def test(self):
        return RED

    def __str__(self):
        string = ""
        for y in range(0, self.length):
            for x in range(0, self.length):
                string += str(self.array[x][y].color) + ' '
            if y < self.length - 1:
                string += '\n'
        return string

###### Main game loop
a = Matrix(4)
print a.test()
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

