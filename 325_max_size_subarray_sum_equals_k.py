# O(n^2)
# def max_subarray_len(nums, k):
#     if not nums:
#         return 0
#
#     ans = 0
#     preSum = [0] * len(nums)
#     preSum[0] = nums[0]
#     for i in range(1, len(nums)):
#         preSum[i] = preSum[i - 1] + nums[i]
#
#     for start in range(len(nums)):
#         for end in range(start, len(nums)):
#             if preSum[end] - preSum[start] + nums[start] == k:
#                 ans = max(ans, end - start + 1)
#
#     return ans

# O(n)
def max_subarray_len(nums, k):
    if not nums:
        return 0

    ans = 0
    preSum = {}
    preSum[0] = -1
    cSum = 0
    for i in range(len(nums)):
        cSum += nums[i]
        if cSum - k in preSum:
            ans = max(ans, i - preSum[cSum - k])
        if cSum not in preSum:
            preSum[cSum] = i

    return ans

# print(max_subarray_len([1, -1, 5, -2, 3], 3))
print(max_subarray_len([-2, -1, 2, 1], 1))
