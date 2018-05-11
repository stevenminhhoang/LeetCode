def remove_element(nums, val):
    v = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[v], nums[i] = nums[i], nums[v]
            v += 1

    return nums[:v], v

print(remove_element([3, 2, 2, 3, 3, 4, 3], 3))
