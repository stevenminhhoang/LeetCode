def climb_stairs_memo(n, memo):
    # Memoization
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] == 0:
        memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]


def climb_stairs(n):
    memo = [0 for i in range(n + 1)]
    # return climb_stairs_memo(n, memo)
    return climb_stairs_dp(n)


def climb_stairs_dp(n):
    # DP
    memo = [0 for i in range(n + 1)]
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]

print(climb_stairs(3))
