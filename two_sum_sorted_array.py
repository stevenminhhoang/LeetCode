# using two-pointers technique
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        two_sum = nums[left] + nums[right]
        if two_sum == target:
            return [nums[left], nums[right]]
        elif two_sum < target:
            left += 1
        else:
            right -= 1

    return False

# using dictionary
# def two_sum_sorted(nums, target):
#     dic = {}
#     for i, num in enumerate(nums):
#         if target - num in dic:
#             return [dic[target-num]+1, i+1]
#         dic[num] = i




print(two_sum_sorted([1,2,3,4,5], 7))
