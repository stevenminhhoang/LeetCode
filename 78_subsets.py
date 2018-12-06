def subsets(nums):
    nums.sort()
    list = []
    backtrack(list, [], nums, 0)
    return list

def backtrack(list, temp_list, nums, start):
    list.append(temp_list[:])
    for i in range(start, len(nums)):
        temp_list.append(nums[i])
        backtrack(list, temp_list, nums, i + 1)
        temp_list.pop()


print(subsets([1, 2, 3]))
