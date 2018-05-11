def pivot_index(nums):
    s = sum(nums)
    l_sum = 0
    for i in range(len(nums)):
        r_sum = s - l_sum - nums[i]
        if l_sum == r_sum:
            return i
        l_sum += nums[i-1]

    return -1


# print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([-1, -1, -1, 0, 1, 1]))









    # l_sum = 0
    # r_sum = 0
    # left, right = 0, len(nums) - 1
    # while left <= right:
    #     l_sum += nums[left]
    #     r_sum += nums[right]
    #     if l_sum == r_sum:
    #
    #     left += 1
    #     right -= 1





# print(pivot_index([1, 7, 3, 6, 5, 6]))
# print(pivot_index([1, 2, 3]))
