def k_sum(nums, target, k):
    def k_sum_helper(nums, target, k, start):
        res = []
        # Base case
        if k == 2:
            left, right = start, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                if s < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(start, len(nums) - k + 1):
                temp = k_sum_helper(nums, target - nums[i], k - 1, start + 1)
                if temp:
                    ls = []
                    for t in temp:
                        t.insert(0, nums[i])
                        ls.append(t)

                res += tuple(ls)


                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1

        return res


    nums.sort()
    s = set([tuple(x) for x in k_sum_helper(nums, target, k, 0)])
    return list(s)

print(k_sum([1, 0, -1, 0, -2, 2], 0, 4))
