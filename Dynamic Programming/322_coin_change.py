# Recursive
def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    ans = float('inf')

    for coin in coins:
        ans = min(ans, 1 + coin_change_recursive(coins, amount - coin))

    return ans

# print(coin_change_recursive([1, 3, 4], 10))

# Memoization
def coin_change(coins, amount):
    def coin_change_memo(coins, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        if amount in memo:
            return memo[amount]

        best = float('inf')
        for coin in coins:
            res = (coin_change_memo(coins, amount - coin, memo))
            if res >= 0:
                best = min(best, res + 1)

        memo[amount] = best if best < float('inf') else -1
        return memo[amount]

    memo = {}
    return coin_change_memo(coins, amount, memo)

# print(coin_change([1, 3, 4], 10))

# DP
def coin_change_DP(coins, amount):
    dp = [float('inf') for i in range(amount + 1)]
    dp[0] = 0
    for coin in coins:
        for x in range(1, amount + 1):
            if x >= coin:
                dp[x] = min(dp[x], 1 + dp[x - coin])

    return dp[amount] if dp[amount] < float('inf') else -1

print(coin_change_DP([1, 3, 4], 10))
