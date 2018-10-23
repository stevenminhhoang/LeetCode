def max_product(nums):
    maxA = maxB = maxC = float('-inf')
    minA = minB = float('inf')
    for num in nums:
        if num > maxA:
            maxC = maxB
            maxB = maxA
            maxA = num
        elif num > maxB:
            maxC = maxB
            maxB = num
        elif num > maxC:
            maxC = num
        if num < minA:
            minB = minA
            minA = num
        elif num < minB:
            minB = num

    return max(maxA * maxB * maxC, minA * minB * maxA)

print(max_product([1, -4, 3, -6, 7, 0]))
