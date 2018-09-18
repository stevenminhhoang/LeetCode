# O(n^2)
def max_area(height):
    ans = 0
    for i in range(len(height) - 1):
        for j in range(i + 1, len(height)):
            area = min(height[i], height[j]) * (j - i)
            ans = max(ans, area)

    return ans


# print(max_area([1,8,6,2,5,4,8,3,7]))

# O(n)
def area(height):
    ans = 0
    left, right = 0, len(height) - 1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        ans = max(ans, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return ans

print(area([1,8,6,2,5,4,8,3,7]))
