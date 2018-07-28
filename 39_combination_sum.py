def combination_sum(nums, target):
    def backtrack(lis, nums, combination, start, target):
        if target < 0:
            return
        if target == 0:
            lis.append(combination[:])

        else:
            for i in range(start, len(nums)):
                combination.append(nums[i])
                backtrack(lis, nums, combination, i, target - nums[i])
                # backtrack
                combination.pop()

    lis = []
    backtrack(lis, nums, [], 0, target)
    return lis

print(combination_sum([2,3,6,7], 7))
