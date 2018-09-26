# O(n^2)
def three_sum(nums, target):
    ans = set()
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == target:
                ans.add((nums[i], nums[l], nums[r]))
            if nums[i] + nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

    return [list(x) for x in ans]

print(three_sum([-1, 0, 1, 2, -1, -4], 0))
