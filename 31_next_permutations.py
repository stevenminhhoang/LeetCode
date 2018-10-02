# O(n)
def next_permutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1:] = nums[i + 1:][::-1]

    return nums

print(next_permutation([1,2,3]))
print(next_permutation([3,2,1]))
print(next_permutation([1,1,5]))
print(next_permutation([1,5,8,4,7,6,5,3,1]))
