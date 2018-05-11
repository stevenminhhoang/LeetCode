def maximum_subarray_size_k(arr, k):
    # O(n * k) solution for finding maximum sum of a subarray of size k
    # max_sum = 0
    # n = len(arr)
    # for i in range(n - k + 1):
    #     current_sum = 0
    #     for j in range(k):
    #         current_sum += arr[i + j]
    #     max_sum = max(max_sum, current_sum)
    #
    # return max_sum


    # 0(n) solution for finding maximum sum of a subarray of size k
    max_sum = 0
    n = len(arr)
    for i in range(k):
        max_sum += arr[i]

    window_sum = max_sum
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


print(maximum_subarray_size_k([5,2,-1,0,3], 3))
