# O(log(n))
def find_min_rotated_sorted_array(nums):
    if len(nums) == 1:
        return nums[0]

    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] < nums[right]:
            return nums[left]

        mid = left + (right - left) // 2
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


# print(find_min_rotated_sorted_array([4,5,6,7,0,1,2]))
# print(find_min_rotated_sorted_array([3,4,5,1,2]))
# print(find_min_rotated_sorted_array([2, 1]))
print(find_min_rotated_sorted_array([3, 1, 2]))
