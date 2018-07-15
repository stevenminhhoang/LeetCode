# Memoization
def LIS_recursive(nums):
    def helper(nums, index, memo):
        if index == len(nums) - 1:
            return 1

        if index in memo:
            return memo[index]

        ans = 1
        for i in range(index + 1, len(nums)):
            if nums[index] < nums[i]:
                ans = max(ans, 1 + helper(nums, i, memo))

        memo[index] = ans
        return ans

    if not nums:
        return 0

    memo = {}
    return max([helper(nums, i, memo) for i in range(len(nums))])

# print(LIS_recursive([1,3,6,7,9,4,10,5,6]))
# print(LIS_recursive([10,9,2,5,3,7,101,18]))


# DP
def longest_increasing_subsequence(nums):
    ans = 1
    dp = [1 for i in range(len(nums))]
    for i in range(1, len(dp)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                ans = max(ans, dp[i])

    return ans

print(longest_increasing_subsequence([1,3,6,7,9,4,10,5,6]))
