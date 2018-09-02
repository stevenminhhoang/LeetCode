# O(max(m, n) * log(max(m, n)))
def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return res


print(intersection([4,5,9], [4,4,8,9,9]))
