def peak_index(A):
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

print(peak_index([0,2,1,0]))
