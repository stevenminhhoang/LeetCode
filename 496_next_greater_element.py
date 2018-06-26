def next_greater_element(findNums, nums):
    ans = []
    dic = {}
    stack = []
    for x in nums:
        while len(stack) > 0 and stack[-1] < x:
            dic[stack.pop()] = x
        stack.append(x)

    for x in findNums:
        ans.append(dic.get(x, -1))

    return ans

print(next_greater_element([4,1,2], [1,3,4,2]))
print(next_greater_element([2,4], [1,2,3,4]))
