# O(9!)
def combination_sum_III(k, n):
    def backtrack(lis, temp, start, k, n):
        if n < 0:
            return
        if k == 0 and n == 0:
            lis.append(temp[:])
            return
        if k == 0:
            return
        for i in range(start, 10):
            temp.append(i)
            backtrack(lis, temp, i + 1, k - 1, n - i)
            temp.pop()

    if n == 0 or k == 0:
        return []
    lis = []
    backtrack(lis, [], 1, k, n)
    return lis

print(combination_sum_III(3, 7))
