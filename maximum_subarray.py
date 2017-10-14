def maxSubArray(nums):
    ans = 0
    current_sum = nums[0]
    for i in nums[1:]:
        current_sum = max(i,current_sum + i)
        if current_sum > ans:
            ans = current_sum

    print(ans)


maxSubArray([1,2,-1,-4])
