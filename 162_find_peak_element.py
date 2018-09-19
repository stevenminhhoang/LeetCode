# O(n)
# def peak_element(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] > nums[i + 1]:
#             return i
#
#     return len(nums) - 1

def peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left



print(peak_element([1,2,3,1]))
print(peak_element([1,2,1,3,5,6,4]))
