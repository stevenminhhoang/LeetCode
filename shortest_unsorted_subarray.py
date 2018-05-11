def shortest_unsorted_subarray(nums):
    sorted_nums = sorted(nums)
    start = len(nums)
    end = 0
    for i in range(len(nums)):
        if sorted_nums[i] != nums[i]:
            start = min(start, i)
            end = max(end, i)

    if end >= start:
        return end - start + 1
    else:
        return 0

print(shortest_unsorted_subarray([2, 4, 6, 8, 9, 10, 9, 15]))
print(shortest_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]))
