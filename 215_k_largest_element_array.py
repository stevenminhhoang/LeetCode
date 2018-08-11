# O(n + k*log(n))
import heapq

def k_largest_element(nums, k):
    if not nums:
        return 0
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)

    return nums[0]


print(k_largest_element([3,2,1,5,6,4], 2))
print(k_largest_element([3,2,3,1,2,4,5,5,6], 4))
