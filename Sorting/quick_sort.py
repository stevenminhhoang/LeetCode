import random
# def quick_sort(nums):
#     def q_sort(nums, left, right):
#         if left >= right:
#             return
#
#         pivot = random.randint(left, right)
#
#         # move pivot to first index
#         nums[pivot], nums[left] = nums[left], nums[pivot]
#         # partition
#         i = left
#         for j in range(left + 1, right + 1):
#             if nums[j] < nums[left]:
#                 i += 1
#                 nums[i], nums[j] = nums[j], nums[i]
#
#         # move pivot back to proper position
#         nums[i], nums[left] = nums[left], nums[i]
#
#         q_sort(nums, left, i - 1)
#         q_sort(nums, i + 1, right)
#
#
#     q_sort(nums, 0, len(nums) - 1)
#     return nums

def quicksort(nums):
    def qsort(nums, left, right):
        if left >= right:
            return

        pivot = nums[left]
        i = left
        for j in range(left + 1, right + 1):
            if nums[j] < pivot:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]

        nums[i], nums[left] = nums[left], nums[i]
        qsort(nums, left, i - 1)
        qsort(nums, i + 1, right)

    qsort(nums, 0, len(nums) - 1)
    return nums



# print(quick_sort([54,26,93,17,77,31,44,55,20]))
print(quicksort([54,26,93,17,77,31,44,55,20]))
