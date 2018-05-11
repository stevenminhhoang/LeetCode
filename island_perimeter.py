def num_of_neighbors(cell, i, j):
    count = 0
    if i > 0 and cell[i - 1][j] == 1:
        count += 1
    if i < len(cell) - 1 and cell[i + 1][j] == 1:
        count += 1
    if j > 0 and cell[i][j - 1] == 1:
        count += 1
    if j < len(cell[0]) - 1 and cell[i][j + 1] == 1:
        count += 1

    return count


def island_perimeter(grid):
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4 - num_of_neighbors(grid, i, j)

    return perimeter


print(island_perimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))
