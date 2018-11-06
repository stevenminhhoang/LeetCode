# O(n * log(n))
def min_move(nums):
    nums.sort()
    count = 0
    i, j = 0, len(nums) - 1
    while i < j:
        count += nums[j] - nums[i]
        i += 1
        j -= 1

    return count


print(min_move([1,2,3,6]))
