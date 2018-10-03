# O(n^2)
def maxProduct(nums):
    ans = nums[0]
    for i in range(len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod = prod * nums[j]
            ans = max(ans, prod)

    return ans

# O(n)
def maxProduct(self, nums):
    max_arr = [0] * len(nums)
    min_arr = [0] * len(nums)
    max_arr[0] = min_arr[0] = nums[0]
    ans = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > 0:
            max_arr[i] = max(nums[i], nums[i] * max_arr[i - 1])
            min_arr[i] = min(nums[i], nums[i] * min_arr[i - 1])
        else:
            max_arr[i] = max(nums[i], nums[i] * min_arr[i - 1])
            min_arr[i] = min(nums[i], nums[i] * max_arr[i - 1])

        ans = max(ans, max_arr[i])

    return ans
