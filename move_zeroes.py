def moveZeroes(nums):
    zero = 0 # position of 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            print(nums)
            zero += 1

    return nums

moveZeroes([2, 1, 0, 3, 12])
