def subarray_sum(arr):
    res = 0
    for i in range(len(arr)):
        res += arr[i]*(i+1)*(len(arr)-i)
        print(res)
    return res

print(subarray_sum([1,2,3]))
