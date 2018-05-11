def max_consecutive_ones(nums):
    if 1 not in nums:
        return 0
    ans = 1
    temp_max = 1
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i] and nums[i+1] == 1:
            temp_max += 1
        else:
            ans = max(ans, temp_max)
            temp_max = 1

    return max(ans, temp_max)

print(max_consecutive_ones([1,0,1,1,0,1]))
