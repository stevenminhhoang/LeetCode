def two_sum(nums, k):
    dic = {}
    for num in nums:
        if (k - num) in dic:
            return True
        else:
            dic[num] = k - num

    return False

print(two_sum([10, 15, 3, 14], 17))
