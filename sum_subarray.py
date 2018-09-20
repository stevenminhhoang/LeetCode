def subarray_sum(arr):
    n = len(arr)
    ans = 0
    for i in range(len(arr)):
        ans += arr[i] * (n - i) * (i + 1)

    return ans

print(subarray_sum([1, 2, 3, 4]))
