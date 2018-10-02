class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.nums = nums
        if len(self.nums) > 0:
            self.preSum = [0] * len(nums)
            self.preSum[0] = nums[0]
            for i in range(1, len(nums)):
                self.preSum[i] = self.preSum[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.preSum[j] - self.preSum[i] + self.nums[i]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
