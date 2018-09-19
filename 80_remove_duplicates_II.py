# O(n)
def remove_duplicates_II(nums):
    i = 0
    for j in range(len(nums)):
        if i < 2 or nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1

    return nums[:i]

print(remove_duplicates_II([0,0,1,1,1,1,2,3,3]))
