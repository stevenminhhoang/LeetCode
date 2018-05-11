def search_insert(nums, target):
    low = 0
    high = len(nums) - 1
    found = False

    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)

    while low <= high:
         mid = (low + high) // 2
         if nums[mid] == target:
             return mid
         elif nums[mid] < target:
             low = mid + 1
         else:
             high = mid - 1

    return low

print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 2))
print(search_insert([1, 3, 5, 6], 7))
print(search_insert([1, 3, 5, 6], 0))
print(search_insert([1, 2, 3, 4, 5, 6], 3))
print(search_insert([1, 3, 5, 8], 8))
print(search_insert([1, 3, 5, 7], 4))
