O(n)
def subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0

    start, end = 0, 0
    prod = 1
    count = 0
    while end < len(nums):
        prod *= nums[end]
        while prod >= k:
            prod /= nums[start]
            start += 1

        count += end - start + 1
        end += 1


    return count

print(subarray_product_less_than_k([10, 5, 2, 6], 100))
