# O(k * log(k))
import heapq
def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    ans = []
    count = 0
    heap = [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
    while heap and count < k:
        sum, i, j = heapq.heappop(heap)
        count += 1
        ans.append([nums1[i], nums2[j]])
        heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return ans


print(k_smallest_pairs([4,3,2,2], [4,3,2,1], 4))
