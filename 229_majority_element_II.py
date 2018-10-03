def majorityElement(nums):
    if not nums:
        return []

    candidate1, candidate2 = None, None
    count1, count2 = 0, 0
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    res = []
    if nums.count(candidate1) > len(nums) // 3:
        res.append(candidate1)
    if nums.count(candidate2) > len(nums) // 3:
        res.append(candidate2)

    return res
