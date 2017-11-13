def majority_element(nums):
    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    for key,val in dic.items():
        if val > len(nums) // 2:
            return key

print(majority_element([1,2,3,3,4,3,3]))
