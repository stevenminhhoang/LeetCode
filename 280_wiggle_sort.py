# O(n * log(n))
def wiggle_sort(nums):
    nums.sort()
    for i in range(1, len(nums) - 1, 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

print(wiggle_sort([3,5,2,1,6,4]))

# O(n)
def wigglesort(nums):
    for i in range(len(nums) - 1):
        if i % 2 == 0 and nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        if i % 2 == 1 and nums[i] < nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

print(wigglesort([3,5,2,1,6,4]))
