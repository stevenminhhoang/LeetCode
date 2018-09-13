def wiggle_sort_II(nums):
    for i in range(len(nums) - 1):
        if i % 2 == 0 and nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        if i % 2 == 1 and nums[i] < nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

print(wiggle_sort_II([1, 5, 1, 1, 6, 4]))
