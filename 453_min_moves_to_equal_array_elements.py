def min_moves(nums):
    if not nums:
        return 0

    minX = min(nums)
    move = 0
    for num in nums:
        move += num - minX

    return move


print(min_moves([2,1,3]))
