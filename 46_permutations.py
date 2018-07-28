def permutation(nums):
    list = []
    backtrack(list, nums, 0)
    return list

def backtrack(list, nums, start):
    if start == len(nums):
        list.append(nums[:])
    else:
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(list, nums, start + 1)
            nums[i], nums[start] = nums[start], nums[i]


print(permutation([1, 2, 3]))


# Using visited array:
def permutation_II(nums):
    def backtrack(lis, temp, nums, visited):
        if len(temp) == len(nums):
            lis.append(temp[:])
        else:
            for i in range(len(nums)):
                if visited[i]:
                    continue

                temp.append(nums[i])
                visited[i] = True
                backtrack(lis, temp, nums, visited)
                temp.pop()
                visited[i] = False



    lis = []
    visited = [False for i in range(len(nums))]
    backtrack(lis, [], nums, visited)
    return lis


print(permutation_II([1, 2, 3]))
