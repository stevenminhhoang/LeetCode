# O(log(n))
def search_range(nums, target):
    if not nums:
        return [-1, -1]

    def bs_left(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left if nums[left] == target else -1

    def bs_right(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        return left if nums[left] == target else -1

    return [bs_left(nums, target), bs_right(nums, target)]

print(search_range([5,7,7,8,8,8,10], 8))
