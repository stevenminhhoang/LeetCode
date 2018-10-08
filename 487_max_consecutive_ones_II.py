def max_consecutive_ones_II(nums):
    pre, curr = -1, 0
    ans = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            curr += 1
        else:
            pre = curr
            curr = 0

        ans = max(ans, pre + curr + 1)

    return ans

print(max_consecutive_ones_II([1,0,1,1,0]))
