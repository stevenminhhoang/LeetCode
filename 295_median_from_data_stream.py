class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low = []
        self.high = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -self.low[0])
        heapq.heappop(self.low)
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -self.high[0])
            heapq.heappop(self.high)



    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
