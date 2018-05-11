def maximum_average_subarray(nums, k):
    n = len(nums)
    max_sum = sum(nums[:k])
    window_sum = max_sum

    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return (max_sum / k)

print(maximum_average_subarray([1,12,-5,-6,50,3], 4))
