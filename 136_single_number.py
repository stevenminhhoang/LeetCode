def single_number(nums):
    res = 0
    for num in nums:
        res ^= num

    return res

print(single_number([4,1,2,1,2]))
