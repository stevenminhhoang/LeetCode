def find_disappeared_numbers(nums):
    return list(set(range(1, len(nums)+1)).difference(set(nums)))

print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))
