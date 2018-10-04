# O(n^3)
def four_sum(nums, target):
    if len(nums) < 4:
        return []

    nums.sort()
    res = set()
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s == target:
                    res.add((nums[i], nums[j], nums[left], nums[right]))
                if s < target:
                    left += 1
                else:
                    right -= 1

    return [x for x in res]

print(four_sum([1, 0, -1, 0, -2, 2], 0))
