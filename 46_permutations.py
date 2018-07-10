def permutation(nums):
    list = []
    backtrack(list, nums, 0)
    return list

def backtrack(list, nums, start):
    if start == len(nums):
        list.append(nums[:])
    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        backtrack(list, nums, start + 1)
        nums[i], nums[start] = nums[start], nums[i]


print(permutation([1, 2, 3]))
