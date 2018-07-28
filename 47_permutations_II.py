def permutation_unique(nums):
    def backtrack(lis, visited, nums, temp):
        if len(temp) == len(nums):
            lis.append(temp[:])
            print("Ans: {0}".format(lis))

        for i in range(0, len(nums)):
            if visited[i] == True:
                continue
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                continue

            temp.append(nums[i])
            visited[i] = True
            print(temp)
            print("Visited: {0}".format(visited))
            backtrack(lis, visited, nums, temp)
            # backtrack
            temp.pop()
            visited[i] = False
            print("Backtrack: {0}".format(temp))
            print("Visited: {0}".format(visited))

    nums.sort()
    lis = []
    visited = [False for i in range(len(nums))]
    backtrack(lis, visited, nums, [])
    return lis

print(permutation_unique([1,1,2]))
