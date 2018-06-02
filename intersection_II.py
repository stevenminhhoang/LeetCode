from collections import Counter
def intersect(nums1, nums2):
    ans = []
    dict1 = Counter(nums1)
    dict2 = Counter(nums2)
    intersection = dict1 & dict2
    for key, count in intersection.items():
        for _ in range(count):
            ans.append(key)
    return ans

print(intersect([1, 2, 2, 1], [2, 2]))
