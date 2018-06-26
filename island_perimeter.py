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

# DFS
def islandPerimeter(self, grid):
    def dfs(grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 1
        if grid[row][col] == 0:
            return 1
        if grid[row][col] == -1:
            return 0

        count = 0
        grid[row][col] = -1
        count += dfs(grid, row - 1 , col)
        count += dfs(grid, row + 1, col)
        count += dfs(grid, row, col - 1)
        count += dfs(grid, row, col + 1)

        return count

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                return dfs(grid, row, col)

print(island_perimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))
