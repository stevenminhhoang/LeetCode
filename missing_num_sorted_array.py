def missing_num_sorted_array(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] != mid and nums[mid - 1] == mid - 1:
            return mid
        elif nums[mid] != mid:
            right = mid - 1
        else:
            left = mid + 1

    return left

print(missing_num_sorted_array([0,1,2,4,5,6,7]))
print(missing_num_sorted_array([0,1,2,3,4,5]))
print(missing_num_sorted_array([1,2,3,4]))
