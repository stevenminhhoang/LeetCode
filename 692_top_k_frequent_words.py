# O(n + k*log(n))
import collections, heapq
def top_k_frequent_words(words, k):
    count = collections.Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for i in range(k)]


print(top_k_frequent_words(["love", "leetcode", "i", "i", "love", "coding"], 2))
