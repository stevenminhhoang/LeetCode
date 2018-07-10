# Memoization
def unique_path_II(grid):
    def count_paths_II(grid, r, c, memo):
        if not (0 <= r < row and 0 <= c < col):
            return 0
        if r == row - 1 and c == col - 1:
            return 1
        if grid[r][c] == 1:
            return 0

        key = (r, c)
        if key not in memo:
            memo[key] = count_paths_II(grid, r + 1, c, memo) + count_paths_II(grid, r, c + 1, memo)

        return memo[key]

    row, col = len(grid), len(grid[0])
    memo = {}
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return 0
    return count_paths_II(grid, 0, 0, memo)


# DP
# def unique_path_II(grid):
#     row, col = len(grid), len(grid[0])
#     dp = [[0 for j in range(col)] for i in range(row)]
#     if grid[0][0] == 1:
#         return 0
#     dp[0][0] = 1
#
#     for r in range(row):
#         for c in range(col):
#             if grid[r][c] == 1:
#                 dp[r][c] = 0
#             elif r == 0 and c > 0:
#                 dp[r][c] = dp[r][c - 1]
#             elif c == 0 and r > 0:
#                 dp[r][c] = dp[r - 1][c]
#             elif r > 0 and c > 0:
#                 dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
#
#     return dp[-1][-1]





# print(unique_path_II([[0, 1]]))
print(unique_path_II([[0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0],[0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0],[0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,0,1,0],[0,0,1,1,1,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1],[0,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,1],[0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0],[1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1],[0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1],[1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],[1,1,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1],[0,0,1,0,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0],[0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1],[0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1],[0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,1,0],[0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1],[0,0,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1],[0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0],[0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,0,0,0],[1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1],[0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0],[0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1],[1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0],[1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],[1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0],[1,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0],[1,0,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0],[0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0],[0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0],[0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,1],[0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]]))
