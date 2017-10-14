def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    for key, val in dic.items():
        if val == 1:
            return key

print(singleNumber([1,1,2,2,3]))
