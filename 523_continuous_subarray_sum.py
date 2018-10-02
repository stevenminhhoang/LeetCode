# O(n^2)
# def continuous_subarray_sum(nums, k):
#     for i in range(len(nums) - 1):
#         s = nums[i]
#         for j in range(i + 1, len(nums)):
#             s += nums[j]
#             if k == 0 and s == 0:
#                 return True
#             elif k != 0 and s % k == 0:
#                 return True
#
#     return False

# O(n^2)
# def continuous_subarray_sum(nums, k):
#     preSum = [0] * len(nums)
#     preSum[0] = nums[0]
#     for i in range(1, len(nums)):
#         preSum[i] = preSum[i - 1] + nums[i]
#
#     for start in range(len(nums) - 1):
#         for end in range(start + 1, len(nums)):
#             s = preSum[end] - preSum[start] + nums[start]
#             if s == k or (k != 0 and s % k == 0):
#                 return True
#
#     return False

# O(n)
def continuous_subarray_sum(nums, k):
    dic = {}
    dic[0] = -1
    cSum = 0
    for i in range(len(nums)):
        cSum += nums[i]
        if k != 0:
            cSum = cSum % k
        if cSum in dic:
            if i - dic[cSum] > 1:
                return True

        dic[cSum] = i

    return False



print(continuous_subarray_sum([23, 2, 4, 6, 7], 6))
