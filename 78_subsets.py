def subsets(nums):
    nums.sort()
    list = []
    backtrack(list, [], nums, 0)
    return list

def backtrack(list, temp_list, nums, start):
    list.append(temp_list[:])
    print("Ans: {0}" .format(list))
    for i in range(start, len(nums)):
        temp_list.append(nums[i])
        print(temp_list)
        backtrack(list, temp_list, nums, i + 1)
        temp_list.pop()
        print(temp_list)


print(subsets([1, 2, 3]))
