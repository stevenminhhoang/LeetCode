# O(n + k*log(n))
import collections, heapq
def top_k_frequent_nums(nums, k):
    count = collections.Counter(nums)
    heap = [(-freq, num) for num, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]

print(top_k_frequent_nums([4,1,-1,2,-1,2,3], 2))
