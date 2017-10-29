def remove_duplicate(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    print(nums[:i+1])

    return i + 1

print(remove_duplicate([1,1,2]))
print(remove_duplicate([1,1,1,2,2,4,5,6]))
