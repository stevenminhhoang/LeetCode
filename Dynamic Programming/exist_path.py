def exist_path(grid):
    row, col = len(grid), len(grid[0])
    dp = [[0 for j in range(col)] for i in range(row)]
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return False
    dp[0][0] = 1

    for i in range(1, row):
        if grid[i][0] == 1:
            dp[i][0] = 0
        else:
            dp[i][0] = dp[i - 1][0]

    for j in range(1, col):
        if grid[0][j] == 1:
            dp[0][j] = 0
        else:
            dp[0][j] = dp[0][j - 1]

    for i in range(1, row):
        for j in range(1, col):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


    return (dp[-1][-1] > 0)

print(exist_path([[0, 0, 0, 1, 0],
                  [1, 0, 0, 0, 1],
                  [0, 1, 0, 0, 1],
                  [1, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0]]))
