def subsets_II(nums):
    nums.sort()
    list = []
    backtrack(list, [], nums, 0)
    return list

def backtrack(list, temp, nums, start):
    list.append(temp[:])
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue
        temp.append(nums[i])
        backtrack(list, temp, nums, i + 1)
        temp.pop()

print(subsets_II([1, 2, 2, 3]))
