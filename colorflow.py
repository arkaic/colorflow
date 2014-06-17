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
            self.adjacents[0] = cell
        elif direction == 'E':
            self.adjacents[1] = cell
        elif direction == 'S':
            self.adjacents[2] = cell
        elif direction == 'W':
            self.adjacents[3] = cell

    def visit(self):
        self.visited = True

    def is_visited(self):
        return self.visited

    #If this cell is out of bounds, its color shall be 0.
    def is_out_of_bounds(self):
        return self.color == 0


length = raw_input('What length do you want for the matrix?: ')

matrix = [[0 for x in xrange(int(length))] for y in xrange(int(length))]
print("Color Flow --------")
print("Size of matrix is " + str(len(matrix)))

#Make and print matrix
#TODO - make random number
for x in range(0, len(matrix)):
    for y in range(0, len(matrix[x])):
        rand_color = 7
        matrix[x][y] = Cell(rand_color, (x,y))


#Make and set adjacents
for x in range(0, len(matrix)):
    for y in range(0, len(matrix[x])):
        fcell = matrix[x][y]
        xw = x - 1
        xe = x + 1
        yn = y - 1
        ys = y + 1

        if yn < 0:
            fcell.set_adjacent(Cell(0, (x, yn)), "N")
        else:
            fcell.set_adjacent(matrix[x][yn], "N")

        if xe >= len(matrix):
            fcell.set_adjacent(Cell(0, (xe, y)), "E")
        else: 
            fcell.set_adjacent(matrix[xe][y], "E")

        if ys >= len(matrix):
            fcell.set_adjacent(Cell(0, (x, ys)), "S")
        else:
            fcell.set_adjacent(matrix[x][ys], "S")

        if xw < 0:
            fcell.set_adjacent(Cell(0, (xw, y)), "W")
        else:
            fcell.set_adjacent(matrix[xw][y], "W")

        print(fcell)
        print(" " + str(fcell.adjacents[0]))
        print(" " + str(fcell.adjacents[1]))
        print(" " + str(fcell.adjacents[2]))
        print(" " + str(fcell.adjacents[3]))



print("")
print("Matrix created.........")
print("")


#Depth First Search
def traversal_algorithm1(cell):
    visited_cell_count = 0
    total_cell_count = len(matrix) * len(matrix)
    open_cells = [cell]

    while visited_cell_count != total_cell_count and len(open_cells) > 0:
        while open_cells[-1].is_visited():
            open_cells.pop()

        current_cell = open_cells.pop()
        current_cell.visit()
        visited_cell_count += 1

        print(current_cell)
        for adj_cell in current_cell.adjacents:
            if not adj_cell.is_out_of_bounds():
                open_cells.append(adj_cell)
                print("appended")

    print(str(visited_cell_count) + " cells have been visited")



cell = matrix[0][0]
slist = [cell]
traversal_algorithm1(cell)