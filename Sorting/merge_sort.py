# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     mid = len(nums) // 2
#     left = nums[:mid]
#     right = nums[mid:]
#     merge_sort(left)
#     merge_sort(right)
#
#     i, j = 0, 0
#     k = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             nums[k] = left[i]
#             i += 1
#         else:
#             nums[k] = right[j]
#             j += 1
#
#         k += 1
#
#     while i < len(left):
#         nums[k] = left[i]
#         k += 1
#         i += 1
#
#
#     while j < len(right):
#         nums[k] = right[j]
#         k += 1
#         j += 1
#
#
#     # return nums

def merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res += left[i:]
    res += right[j:]
    return res


def mergesort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    return merge(left, right)

# print(merge_sort([54,26,93,17,77,31,44,55,20]))

print(mergesort([54,26,93,17,77,31,44,55,20]))
