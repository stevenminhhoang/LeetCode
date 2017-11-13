def array_pair_sum(nums):
    res = 0
    n = len(nums)
    nums.sort()
    for i in range(0,n-1,2):
        res += min(nums[i],nums[i+1])

    return res

print(array_pair_sum([1,4,3,2]))
