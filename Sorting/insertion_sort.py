def insertion_sort(nums):
    for i in range(len(nums)):
        current = nums[i]
        j = i
        while j > 0 and current < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1

        nums[j] = current

    return nums


print(insertion_sort([54,26,93,17,77,31,44,55,20]))
