import collections
# O(n^2)
def subarray_sum_k(nums, k):
    count = 0
    prefix = [0] * (len(nums))
    prefix[0] = nums[0]
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i - 1] + nums[i]

    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if prefix[j] - prefix[i] + nums[i] == k:
                count += 1

    return count

# O(n)
# def subarray_sum_k(nums, k):
#     count = 0
#     cSum = 0
#     dic = collections.Counter()
#     dic[0] = 1
#     for i in range(len(nums)):
#         cSum += nums[i]
#         if cSum - k in dic:
#             count += dic[cSum - k]
#
#         dic[cSum] += 1
#
#     return dic



print(subarray_sum_k([1,1,1], 2))
# print(subarray_sum_k([1,3,4,8,6,1,4,2], 19))
