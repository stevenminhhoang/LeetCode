def num_distinct_islands(grid):
    def dfs(grid, row, col, path):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1):
            return ""

        grid[row][col] = 0
        return path + dfs(grid, row - 1, col, "d") + "u" + dfs(grid, row + 1, row, col, "u") + "d" + dfs(grid, row, col - 1, "r") + "l" + dfs(grid, row, col + 1, "l") + "r"



    ans = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                path = dfs(grid, i, j, "s")
                print(path)
                ans.add(path)

    return len(ans)


print(num_distinct_islands([[1,1,0,0,0],
[1,1,0,0,0],
[0,0,0,1,1],
[0,0,0,1,1]]))
