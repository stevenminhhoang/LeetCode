# O(n^2)
# def trapping_rain_water(height):
#     ans = 0
#     for i in range(1, len(height) - 1):
#         max_left, max_right = 0, 0
#         for j in range(i + 1):
#             max_left = max(max_left, height[j])
#         for j in range(i, len(height)):
#             max_right = max(max_right, height[j])
#
#         ans += min(max_left, max_right) - height[i]
#
#     return ans


# O(n) DP
# def trapping_rain_water(height):
#     ans = 0
#     n = len(height)
#     left_max = [0] * n
#     right_max = [0] * n
#
#     left_max[0] = height[0]
#     right_max[0] = height[n - 1]
#     for i in range(1, n):
#         left_max[i] = max(left_max[i - 1], height[i])
#     for i in reversed(range(n - 1)):
#         right_max[i] = max(right_max[i + 1], height[i])
#
#     for i in range(1, n - 1):
#         ans += min(left_max[i], right_max[i]) - height[i]
#
#     return ans

# O(n)
def trapping_rain_water(height):
    if not height:
        return 0

    ans = 0
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                ans += left_max - height[left]

            left += 1

        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                ans += right_max - height[right]

            right -= 1

    return ans


print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
