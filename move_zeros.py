def move_zero(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums

print(move_zero([2, 4, 0, 4, 0, 3, 1]))
