def combination(nums, k):
    def backtrack(lis, temp, nums, start, k):
        if len(temp) == k:
            lis.append(temp[:])

        for i in range(start, len(nums)):
            temp.append(nums[i])
            backtrack(lis, temp, nums, i + 1, k)
            temp.pop()

    lis = []
    backtrack(lis, [], nums, 0, k)
    return lis

print(combination([1, 2, 3, 4], 3))
