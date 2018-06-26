def numIslands(grid):
    def dfs(grid, row, col):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            return
        if grid[row][col] == 0:
            return
        grid[row][col] = 0

        dfs(grid, row - 1, col)
        dfs(grid, row + 1, col)
        dfs(grid, row, col - 1)
        dfs(grid, row, col + 1)


    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                count += 1
                dfs(grid, row, col)

    return count

print(numIslands([[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]))
