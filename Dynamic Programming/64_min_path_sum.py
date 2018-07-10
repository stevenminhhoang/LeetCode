def min_path_sum_memo(grid):
    def min_path_sum_helper(grid, row, col, memo):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            return float('inf')
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return grid[row][col]

        if memo[row][col] == 0:
            memo[row][col] = min(min_path_sum_helper(grid, row + 1, col, memo), min_path_sum_helper(grid, row, col + 1, memo)) + grid[row][col]

        return memo[row][col]

    memo = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
    return min_path_sum_helper(grid, 0, 0, memo)


# DP
def min_path_sum(grid):
    dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
    dp[0][0] = grid[0][0]
    for i in range(1, len(grid)):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for j in range(1, len(grid[0])):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
            dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]



    return dp[-1][-1]

# print(min_path_sum([
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]))

print(min_path_sum_memo([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
