# def fib(n, memo):
    # Memoization
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # if memo[n] == 0:
    #     memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    #
    # return memo[n]

def fib(n):
    # Bottom-up DP
    if n == 0:
        return 0
    if n == 1:
        return 1

    memo = [0 for i in range(n)]
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n - 1] + memo[n - 2]

    # 0(1) space
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c




# x = [0 for i in range(100)]
# print(fib(99, x))
print(fib(6))
