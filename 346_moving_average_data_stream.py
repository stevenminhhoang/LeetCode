class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque()
        self.size = size
        self.curr_sum = 0


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.curr_sum += val
        if len(self.queue) == self.size:
            self.curr_sum -= self.queue.popleft()

        self.queue.append(val)
        return float(self.curr_sum) / len(self.queue)






# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
