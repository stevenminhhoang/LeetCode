def three_sum_closest(nums, target):
    res = nums[0] + nums[1] + nums[-1]
    nums.sort()
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == target:
                return s
            if s < target:
                l += 1
            else:
                r -= 1
            if abs(s - target) < abs(res - target):
                res = s

    return res


print(three_sum_closest([-1, 2, 1, -4], 1))
