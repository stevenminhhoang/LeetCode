# O(n + k*log(k))
import collections, heapq

def frequency_sort(s):
    if not s:
        return ""

    count = collections.Counter(s)
    heap = []
    for char, freq in count.items():
        heapq.heappush(heap, (-freq, char))
    ans = ""
    while heap:
        char = heapq.heappop(heap)
        ans += char[1] * abs(char[0])

    return ans


print(frequency_sort("tree"))
print(frequency_sort("Aabb"))
