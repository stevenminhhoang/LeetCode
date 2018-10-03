# O(n^2)
# def three_sum_smaller(nums, target):
#     def binary_search(nums, start, target):
#         left, right = start, len(nums) - 1
#         while left < right:
#             mid = (left + right + 1) // 2
#             if nums[mid] < target:
#                 left = mid
#             else:
#                 right = mid - 1
#
#         return left
#
#
#     def two_sum_smaller(nums, start, target):
#         count = 0
#         for i in range(start, len(nums)):
#             j = binary_search(nums, i, target - nums[i])
#             count += j - i
#
#
#         return count
#
#     ans = 0
#     nums.sort()
#     for i in range(len(nums) - 2):
#         ans += two_sum_smaller(nums, i + 1, target - nums[i])
#
#     return ans

# O(n^2)
def three_sum_smaller(nums, target):
    nums.sort()
    count = 0
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

    return count


print(three_sum_smaller([-2,0,1,3], 2))
