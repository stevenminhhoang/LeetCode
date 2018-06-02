import collections

def find_LHS(nums):
    ans = 0
    dic = collections.Counter(nums)
    for key in dic:
        if (key + 1) in dic:
            ans = max(ans, dic.get(key) + dic.get(key + 1))

    return ans


print(find_LHS([1,3,2,2,5,2,3,7]))
