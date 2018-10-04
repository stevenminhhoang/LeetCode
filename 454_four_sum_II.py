# O(n^2)
def fourSumCount(A, B, C, D):
    count = collections.Counter()
    ans = 0
    for a in A:
        for b in B:
            s = a + b
            count[s] += 1

    for c in C:
        for d in D:
            s = c + d
            ans += count.get(-s, 0)

    return ans
