#Cell holding the coordinate and color
#Null cell will have color = 0
class Cell: 
    color = ""
    x = ""
    y = ""
    visited = False
    #Adjacent order   N   E   S   W
    adjacents =     ["", "", "", ""]

    def __init__(self, color, (numx, numy)):
        self.color = color
        self.x = numx
        self.y = numy

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
        visited = True

    def is_visited(self):
        return visited

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
        print(matrix[x][y])


#Make and set adjacents
for x in range(0, len(matrix)):
    for y in range(0, len(matrix[x])):
        cell = matrix[x][y]
        xw = x - 1
        xe = x + 1
        yn = y - 1
        ys = y + 1

        if yn < 0:
            cell.adjacents[0] = Cell(0, (x, yn))
        else:
            cell.adjacents[0] = matrix[x][yn]

        if xe >= len(matrix):
            cell.adjacents[1] = Cell(0, (xe, y))
        else:
            cell.adjacents[1] = matrix[xe][y]

        if ys >= len(matrix):
            cell.adjacents[2] = Cell(0, (x, ys))
        else:
            cell.adjacents[2] = matrix[x][ys]

        if xw < 0:
            cell.adjacents[3] = Cell(0, (xw, y))
        else:
            cell.adjacents[3] = matrix[xw][y]

#Depth First Search
def dfs_traverse(self, cell):
    visited_cells = 0
    open_list = [cell]
    number_of_cells = len(matrix) * len(matrix)

    while visited_cells != number_of_cells and len(open_list) > 0:
        while open_list[-1].is_visited:
            open_list.pop()

        visiting_cell = open_list.pop()
        visiting_cell.visit()
        number_of_cells += 1

        # for adj_cell in visiting_cell.adjacents:
            


