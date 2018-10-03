def two_sum_smaller(nums, start, target):
    def binary_search(nums, start, target):
        left = start
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid - 1

        return left

    count = 0
    nums.sort()
    for i in range(len(nums)):
        j = binary_search(nums, i, target - nums[i])
        count += j - i

    return count


print(two_sum_smaller([-2,0,1,3], 0, 2))
