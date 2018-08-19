# O(n * log(n))
import math
# def factor_combinations(n):
#     def backtrack(res, temp, start, n):
#         if n <= 1:
#             if len(temp) > 1:
#                 res.append(temp[:])
#                 return
#         for i in range(start, int(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 temp.append(i)
#                 backtrack(res, temp, i, n // i)
#                 temp.pop()
#         for i in range(int(math.sqrt(n)), 0, -1):
#             if n % i == 0 and n // i >= start and i * i != n:
#                 temp.append(n // i)
#                 backtrack(res, temp, n // i, i)
#                 temp.pop()
#
#     res = []
#     backtrack(res, [], 2, n)
#     return res



# Method 2
def factor_combinations(n):
    def backtrack(res, factors, temp, start, n):
        if n <= 1:
            if len(temp) > 1:
                res.append(temp[:])
                return
        for i in range(start, len(factors)):
            if n % factors[i] == 0:
                temp.append(factors[i])
                backtrack(res, factors, temp, i, n // factors[i])
                temp.pop()

    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
    for i in range(int(math.sqrt(n)), 0, -1):
        if n % i == 0 and i * i != n:
            factors.append(n // i)

    res = []
    backtrack(res, factors, [], 0, n)
    return res

print(factor_combinations(16))
