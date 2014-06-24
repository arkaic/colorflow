import random
import os
import sys

#Cell holding the coordinate and color
#Null cell will have color = 0
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
        random.seed()
        #Create and fill matrix
        for x in range(0, self.length):
            for y in range(0, self.length):
                random_color = random.randint(1, 7)
                self.array[x][y] = Cell(random_color, (x, y))

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
                cell.set_adjacent(Cell(0, (x, yn)), "N")
            else:
                cell.set_adjacent(matrix.get(x, yn), "N")

            if xe >= matrix.length:
                cell.set_adjacent(Cell(0, (xe, y)), "E")
            else: 
                cell.set_adjacent(matrix.get(xe, y), "E")

            if ys >= matrix.length:
                cell.set_adjacent(Cell(0, (x, ys)), "S")
            else:
                cell.set_adjacent(matrix.get(x, ys), "S")

            if xw < 0:
                cell.set_adjacent(Cell(0, (xw, y)), "W")
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
        visited_cells.append(current_cell)

        for adj_cell in current_cell.adjacents:
            if not adj_cell.is_out_of_bounds():
                if adj_cell.color == prev_color or adj_cell.color == fill_color:
                    cells_to_visit.append(adj_cell)

    print('')

    matrix.uniform_color_count = len(visited_cells)
    for visited_cell in visited_cells:
        visited_cell.unvisit()




################################Main Script####################################
################################           ####################################
os.system('clear')
print('********COLOR COLLAPSE!!!**********')
print ''
print ''
while True:
    length = raw_input('What length do you want for the matrix?: ')
    if length == 'q':
        sys.exit('End game')
    elif int(length) > 1:
        break
    elif int(length) <= 1:
        print 'Length is too small'

matrix = Matrix(int(length))
os.system('clear')

set_adjacent_cells(matrix)
print ''


####Main Loop####
score = 0
while True: 
    print 'Size of matrix is ' + str(matrix.length)
    print ''
    print 'Score: ' + str(score)
    print matrix

    fill_color = raw_input('Enter a color (number) between [1, 7]: ')
    first_cell = matrix.get(0, 0)
    os.system('clear')

    if fill_color == '' or int(fill_color) < 0 or int(fill_color) > 7:
        os.system('clear')
        print 'Try again..'
        print ''
        continue
    elif int(fill_color) == 0:
        print('End game...')
        break
    else:
        traversal_algorithm1(first_cell, int(fill_color))
        score += 1
        # os.system('clear')
        if matrix.uniform_color_count >= matrix.size:
            os.system('clear')
            print 'Final score: ' + str(score)
            print matrix
            print 'Player wins!'
            print ''
            confirmation = raw_input('Play again? (y/n): ')
            if confirmation == 'y' or confirmaton == 'Y':
                continue
            elif confirmation == 'n' or confirmation == 'N':
                break