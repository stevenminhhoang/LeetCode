# O(n * log(n))
def h_index(citations):
    citations.sort()
    i = 0
    for j in range(len(citations)):
        if citations[len(citations) - 1 - j] > j:
            i += 1

    return i

# print(h_index([6, 5, 3, 1, 0]))

# O(n) Bucket sort
def hIndex(citations):
    n = len(citations)
    buckets = [0] * (n + 1)
    for c in citations:
        if c >= n:
            buckets[n] += 1
        else:
            buckets[c] += 1

    count = 0
    for i in range(n, -1, -1):
        count += buckets[i]
        if count >= i:
            return i

    return 0



print(hIndex([3,0,6,1,5]))
