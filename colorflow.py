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

    def set_adjacent(self, Cell, direction):
        if direction == 'N':
            adjacents[0] = Cell
        elif direction == 'E':
            adjacents[1] = Cell
        elif direction == 'S':
            adjacents[2] = Cell
        elif direction == 'W':
            adjacents[3] = Cell

    def visit(self):
        self.visited = True

    def is_visited(self):
        return self.visited

    #If this cell is out of bounds, its color shall be 0.
    def is_out_of_bounds(self):
        return color == 0


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
            fcell.adjacents[0] = Cell(0, (x, yn))
        else:
            fcell.adjacents[0] = matrix[x][yn]

        if xe >= len(matrix):
            fcell.adjacents[1] = Cell(0, (xe, y))
        else:
            fcell.adjacents[1] = matrix[xe][y]

        if ys >= len(matrix):
            fcell.adjacents[2] = Cell(0, (x, ys))
        else:
            fcell.adjacents[2] = matrix[x][ys]

        if xw < 0:
            fcell.adjacents[3] = Cell(0, (xw, y))
        else:
            fcell.adjacents[3] = matrix[xw][y]

        print(fcell)
        print(" " + str(fcell.adjacents[0]))
        print(" " + str(fcell.adjacents[1]))
        print(" " + str(fcell.adjacents[2]))
        print(" " + str(fcell.adjacents[3]))


print("and lastly")
cell1 = matrix[1][0]
print(cell1)
print(" " + str(cell1.adjacents[0]))
print(" " + str(cell1.adjacents[1]))
print(" " + str(cell1.adjacents[2]))
print(" " + str(cell1.adjacents[3]))

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
        c = 0

        print(current_cell)
        for adj_cell in current_cell.adjacents:
            print(" " + str(adj_cell))
            if not adj_cell.is_out_of_bounds:
                open_cells.append(adj_cell)
                c += 1

    print(str(visited_cell_count) + " cells have been visited")

cell = matrix[0][0]
slist = [cell]
traversal_algorithm1(cell)