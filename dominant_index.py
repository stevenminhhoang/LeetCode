def dominant_index(nums):
    # m = max(nums)
    # if all(m >= 2 * x for x in nums if x != m):
    #     return nums.index(m)
    #
    # return -1

    max_1 = 0
    max_2 = 0
    ans = 0

    for i, n in enumerate(nums):
        if n >= max_1:
            max_2 = max_1
            max_1 = n
            ans = i
        elif n > max_2:
            max_2 = n

    return ans if max_1 >= 2 * max_2 else -1
