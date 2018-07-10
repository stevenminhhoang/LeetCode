def stair_k_steps(n, k):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        j = 1
        while j <= k:
            dp[i] += dp[i - j]
            j += 1

    return dp[-1]

print(stair_k_steps(5, 2))
