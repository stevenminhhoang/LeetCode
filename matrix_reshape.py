from collections import deque

def matrix_reshape(nums, r, c):
    q = deque()
    ans = [[0 for x in range(c)] for y in range(r)]
    r_nums = len(nums)
    c_nums = len(nums[0])

    for i in range(r_nums):
        for j in range(c_nums):
            q.append(nums[i][j])


    if r_nums * c_nums != r * c:
        return nums
    else:
        for i in range(r):
            for j in range(c):
                ans[i][j] = q.popleft()
        return ans


print(matrix_reshape([[1,2],[3,4]], 1, 4))
# print(matrix_reshape([[1],[2],[3],[4]], 2, 3))
