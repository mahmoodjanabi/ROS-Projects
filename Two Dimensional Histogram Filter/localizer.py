# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

# Simply Put, the act of sensing is going through the matrix and multiplying the prob of hit or miss to every element
def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    sumOfElements = 0

    for i in range(len(grid)):
      row=[]
      for j in range(len(grid[i])):
        hit = (color == grid[i][j])
        row.append(beliefs[i][j] *(hit * p_hit + (1-hit) * p_miss))
# get the sum of all elements to normalize later
      sumOfElements += sum(row)
      new_beliefs.append(row)

# Normalize by dividing every element by the sum
    for x in range(len(new_beliefs)):
      for y in range(len(new_beliefs[x])):
        new_beliefs[x][y] /= sumOfElements
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
#             pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
