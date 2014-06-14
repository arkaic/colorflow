#Cell holding the coordinate and color
#Null cell will have color = 0
class Cell: 
    color = ""
    x = ""
    y = ""

    def __init__(self, color, (numx, numy)):
        self.color = color
        self.x = numx
        self.y = numy

    def __str__(self):
        return str(self.color) + '(' + str(self.x) + ', ' + str(self.y) + ')'





length = raw_input('What length do you want for the matrix?: ')

matrix = [[0 for x in xrange(int(length))] for y in xrange(int(length))]
print("Color Flow --------")
print("Size of matrix is " + str(len(matrix)))

#Make and print matrix
for x in range(0, len(matrix)):
    for y in range(0, len(matrix[x])):
        matrix[x][y] = Cell(7, (x,y))
        print(matrix[x][y])


