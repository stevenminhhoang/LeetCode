def combination_sum_II(nums, target):
    def backtrack(lis, combination, nums, start, target):
        if target < 0:
            return
        if target == 0:
            lis.append(combination[:])

        else:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                combination.append(nums[i])
                backtrack(lis, combination, nums, i + 1, target - nums[i])
                combination.pop()

    nums.sort()
    lis = []
    backtrack(lis, [], nums, 0, target)
    return lis

print(combination_sum_II([10,1,2,7,6,1,5], 8))
