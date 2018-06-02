import collections

def set_mismatch(nums):
    dic = {}
    duplicate, missing = 0, 0
    for num in nums:
        if num in dic:
            duplicate = num
        else:
            dic[num] = 1
    key = dic.keys()
    n = len(nums)
    missing = (n * (n + 1) // 2) - (sum(nums) - duplicate)

    return [duplicate, missing]

print(set_mismatch([1,2,2,4]))
