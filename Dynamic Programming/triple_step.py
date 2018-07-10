def triple_step(n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp [i - 3]

    return dp[-1]

print(triple_step(5))
