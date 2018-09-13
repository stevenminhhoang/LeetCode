# O(n * log(A)) A is the size of the alphabet
import collections, heapq

def reorganize_string(S):
    res = ""
    count = collections.Counter(S)
    if any(x > (len(S) + 1) // 2 for x in count.values()):
        return ""

    heap = []
    for key, val in count.items():
        heapq.heappush(heap, (-val, key))

    while len(heap) >= 2:
        cnt1, char1 = heapq.heappop(heap)
        cnt2, char2 = heapq.heappop(heap)
        res += char1 + char2
        if cnt1 + 1 < 0:
            heapq.heappush(heap, (cnt1 + 1, char1))
        if cnt2 + 1 < 0:
            heapq.heappush(heap, (cnt2 + 1, char2))

    if heap:
        res += heap[0][1]

    return res




print(reorganize_string("aaab"))
