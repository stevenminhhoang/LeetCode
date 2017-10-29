def rotate_array(nums, k):
    nums[:] = (nums[:-k][::-1] + nums[-k:][::-1])[::-1]
    return nums

print(rotate_array([1,2,3,4,5,6,7],3))
