def sliding_window(arr, k):
    max_sum = 0
    window_sum = 0
    for i in range(k):
        window_sum += arr[i]

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

print(sliding_window([100, 200, 100, 400, 500, 2, 600], 5))
