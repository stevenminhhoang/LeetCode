def factorial(n):
    dp = [0 for i in range(n)]
    dp[0] = 1
    for i in range(1, n):
        dp[i] = i * dp[i - 1]

    return dp[-1]

print(factorial(6))
