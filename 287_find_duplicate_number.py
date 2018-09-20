# O(n*log(n))
def find_duplicate(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        count = 0
        for num in nums:
            if num <= mid:
                count += 1

        if count <= mid:
            left = mid + 1
        else:
            right = mid

    return left

# print(find_duplicate([1,3,4,2,2]))
print(find_duplicate([3,1,3,4,2]))
