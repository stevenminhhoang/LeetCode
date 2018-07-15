def num_LIS(nums):
    ans = 0
    length = [1 for i in range(len(nums))]
    count = [1 for i in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]

    longest = max(length)
    for i in range(len(nums)):
        if length[i] == longest:
            ans += count[i]

    return ans

print(num_LIS([1, 3, 5, 4, 7]))
