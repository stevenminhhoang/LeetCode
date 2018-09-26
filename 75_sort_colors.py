# O(n) 2 pass
# def sort_colors(nums):
#     low = 0
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             nums[i], nums[low] = nums[low], nums[i]
#             low += 1
#
#     high = len(nums) - 1
#     for i in reversed(range(len(nums))):
#         if nums[i] == 2:
#             nums[i], nums[high] = nums[high], nums[i]
#             high -= 1
#
#     return nums

# O(n) 1 pass
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

# print(sort_colors([2,0,2,1,1,0]))
print(sort_colors([2,0,1]))
