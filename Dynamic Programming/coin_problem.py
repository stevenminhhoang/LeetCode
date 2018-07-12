# Recursive
def coin_recursive(coins, amount, i):
    if amount == 0:
        return 1
    if amount < 0:
        return 0

    count = 0

    for coin in range(i, len(coins)):
        count += coin_recursive(coins, amount - coins[coin], coin)

    return count

# print(coin_recursive([1,2,5],5, 0))

# Memoization
def coin_change(coins, amount):
    def coin_memo(coins, amount, index, memo):
        if amount == 0:
            return 1
        if amount < 0 or index >= len(coins):
            return 0

        key = (amount, index)
        if key in memo:
            return memo[key]

        memo[key] = coin_memo(coins, amount - coins[index], index, memo) + coin_memo(coins, amount, index + 1, memo)

        return memo[key]

    memo = {}
    return coin_memo(coins, amount, 0, memo)

# print(coin_change([1, 2, 5], 5))


# DP
# def coin_DP(coins, amount):
    # dp[i][j] : the number of combinations to make up amount j by using the first i types of coins
    # dp = [[0 for j in range(amount + 1)] for i in range(len(coins))]
    # for i in range(amount + 1):
    #     dp[0][i] = 1
    #
    #
    # for i in range(1, len(coins)):
    #     for j in range(amount + 1):
    #         if j >= coins[i]:
    #             dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
    #         else:
    #             dp[i][j] = dp[i - 1][j]
    #
    # return dp[-1][-1]

# print(coin_DP([1, 2, 5], 5))

# DP 1-D Array
def coin_DP(coins, amount):
    dp = [0 for i in range(amount + 1)]
    dp[0] = 1
    for coin in coins:
        for x in range(1, amount + 1):
            if x >= coin:
                dp[x] += dp[x - coin]
    return dp[-1]

print(coin_DP([1, 2, 5], 5))
