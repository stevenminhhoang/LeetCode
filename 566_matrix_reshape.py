def matrix_reshape(nums, r, c):
    if r * c != len(nums) * len(nums[0]):
        return nums

    ans = [[0 for j in range(c)] for i in range(r)]
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            ans[count // c][count % c] = nums[i][j]
            count += 1

    return ans

print(matrix_reshape([[1,2,3],
 [4,5,6]], 1, 6))
