def maximum_gap(nums):
    if len(nums) < 2:
        return 0

    nums.sort()
    ans = 0
    for i in range(1, len(nums)):
        gap = nums[i] - nums[i - 1]
        ans = max(ans, gap)

    return ans

print(maximum_gap([3,6,9,1]))
