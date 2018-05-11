def degree_of_array(nums):
    left = {}
    right = {}
    count = {}
    for i, x in enumerate(nums):
        if x not in left:
            left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1

    ans = len(nums)
    degree = max(count.values())

    for x in count:
        if count[x] == degree:
            ans = min(ans, right[x] - left[x] + 1)

    return ans


print(degree_of_array([1, 3, 2, 2, 3, 1]))
