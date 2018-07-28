# W = 6
def knapsack(W, wt, val):
    dp = [[0 for j in range(W + 1)] for i in range(len(val) + 1)]
    for i in range(len(val) + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            if wt[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]


print(knapsack(7, [1, 3, 4, 5], [1, 4, 5, 7]))
