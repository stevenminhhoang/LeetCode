def product(arr):
    if not arr:
        return []
    prod = 1
    ans = []
    for num in arr:
        prod *= num

    for i in range(len(arr)):
        ans.append(prod // arr[i])

    return ans

print(product([1, 2, 3, 4, 5]))


def product_except_self(nums):
    ans = [1 for i in range(len(nums))]
    curr_product = 1
    for i in range(len(nums)):
        ans[i] = curr_product
        curr_product *= nums[i]

    curr_product = 1
    for i in reversed(range(len(nums))):
        ans[i] *= curr_product
        curr_product *= nums[i]

    return ans

print(product_except_self([1, 2, 3, 4, 5]))
