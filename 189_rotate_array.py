# O(n)
def rotate_array(nums, k):
    def reverse_array(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    k = k % len(nums)
    reverse_array(nums, 0, len(nums) - 1)
    reverse_array(nums, 0, k - 1)
    reverse_array(nums, k, len(nums) - 1)

    return nums

print(rotate_array([1,2,3,4,5,6,7],3))
