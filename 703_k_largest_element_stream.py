class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        self.size = len(self.heap)
        heapq.heapify(self.heap)
        while self.size > k:
            heapq.heappop(self.heap)
            self.size -= 1


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.heap, val)
            self.size += 1
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
