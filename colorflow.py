import random

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
    uniform_color_count = 1

    def __init__(self, n):
        self.array = [[0 for x in xrange(int(n))] for y in xrange(int(n))]
        self.length = n
        self.size = n * n
        random.seed()
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


length = raw_input('What length do you want for the matrix?: ')
matrix = Matrix(int(length))
print("Color Flow --------")
print("Size of matrix is " + str(matrix.length))

#Make and print matrix
# for x in range(0, matrix.length):
#     for y in range(0, matrix.length):
#         random_color = 7
#         mat = matrix.get(x, y)
#         mat = Cell(random_color, (x, y))


#Make and set adjacents
for x in range(0, matrix.length):
    for y in range(0, matrix.length):
        fcell = matrix.get(x, y)
        xw = x - 1
        xe = x + 1
        yn = y - 1
        ys = y + 1

        if yn < 0:
            fcell.set_adjacent(Cell(0, (x, yn)), "N")
        else:
            fcell.set_adjacent(matrix.get(x, yn), "N")

        if xe >= matrix.length:
            fcell.set_adjacent(Cell(0, (xe, y)), "E")
        else: 
            fcell.set_adjacent(matrix.get(xe, y), "E")

        if ys >= matrix.length:
            fcell.set_adjacent(Cell(0, (x, ys)), "S")
        else:
            fcell.set_adjacent(matrix.get(x, ys), "S")

        if xw < 0:
            fcell.set_adjacent(Cell(0, (xw, y)), "W")
        else:
            fcell.set_adjacent(matrix.get(xw, y), "W")

        #Debug purposes
        # print(fcell)
        # print(" " + str(fcell.adjacents[0]))
        # print(" " + str(fcell.adjacents[1]))
        # print(" " + str(fcell.adjacents[2]))
        # print(" " + str(fcell.adjacents[3]))

# Depth First Search
# Non-recursive implementation. unvisited_cells will be the stack that takes in 
# cells that are adjacent to the current cell. At each iteration of the while 
# loop, all consecutive cells on top of the stack that are already visited will 
#be removed. The next cell on top of the stack, hence, is unvisited. It will be
# set to "visited" and then all of its adjacent cells are added onto the stack. 

def traversal_algorithm1(cell, fill_color):
    visited_cell_count = 0
    total_cell_count = matrix.length * matrix.length
    cells_to_visit = [cell]
    visited_cells = []

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
        visited_cells.append(current_cell)
        visited_cell_count += 1
        current_color = current_cell.color
        current_cell.color = fill_color

        for adj_cell in current_cell.adjacents:
            if not adj_cell.is_out_of_bounds():
                if adj_cell.color == current_color:
                    cells_to_visit.append(adj_cell)

    print(str(visited_cell_count) + " cells have been visited")
    print("Visited cell stack size: " + str(len(visited_cells)))
    print('')

    for visited_cell in visited_cells:
        visited_cell.unvisit()
    matrix.uniform_color_count = len(visited_cells)



##########Main loop#############
print ''
score = 0
while True: 
    print 'Score: ' + str(score)
    first_cell = matrix.get(0, 0)
    print matrix
    fill_color = raw_input('Enter a color (number) between [1, 7]: ')
    if fill_color == '0':
        print('End game...')
        break
    traversal_algorithm1(first_cell, int(fill_color))
    score += 1
    if matrix.uniform_color_count >= matrix.size - 1:
        print matrix
        print 'Player wins!'
        print ''
        break