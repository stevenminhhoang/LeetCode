# O(2^n) Space: O(n)
def combinations(n, k):
    def backtrack(lis, temp, n, k, start):
        if k == 0:
            lis.append(temp[:])

        for i in range(start, n + 1):
            temp.append(i)
            backtrack(lis, temp, n, k - 1, i + 1)
            temp.pop()

    lis = []
    backtrack(lis, [], n, k, 1)
    return lis

print(combinations(4, 2))
