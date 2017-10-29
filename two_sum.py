def twoSum(nums, target):
    dic = {}
    for i,n in enumerate(nums):
        if n not in dic:
            dic[target - n] = i
        else:
            return [dic[n], i]



print(twoSum([3,3], 6))
