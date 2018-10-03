# O(n)
def min_subarray_sum(s, nums):
    ans = float('inf')
    start = 0
    cSum = 0
    for end in range(len(nums)):
        cSum += nums[end]
        while cSum >= s:
            ans = min(ans, end - start + 1)
            cSum -= nums[start]

            start += 1

    if ans == float('inf'):
        return 0
    else:
        return ans

print(min_subarray_sum(7, [2,3,1,2,4,3]))
