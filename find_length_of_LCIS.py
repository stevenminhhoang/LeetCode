def find_length_of_LCIS(nums):
    if nums == []:
        return 0
    if len(nums) <= 1:
        return 1
    count = 1
    max_count = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1

    return max_count

# print(find_length_of_LCIS([1,3,5,4,7]))
print(find_length_of_LCIS([2,2,2,2,2]))
