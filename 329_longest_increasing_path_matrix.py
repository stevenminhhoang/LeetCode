# DFS + Memoization
# O(m * n)
def longest_increasing_path(matrix):
    def dfs(matrix, row, col, cache):
        if cache[row][col] != -1:
            return cache[row][col]
        res = 1
        for dir in ((1,0), (0,1), (-1,0), (0,-1)):
            nr, nc = row + dir[0], col + dir[1]
            if not (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[row][col] < matrix[nr][nc]):
                continue
            length = 1 + dfs(matrix, nr, nc, cache)
            res = max(res, length)

        cache[row][col] = res

        return res


    ans = 0
    cache = [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            curr_length = dfs(matrix, row, col, cache)
            ans = max(ans, curr_length)

    return ans

print(longest_increasing_path([
  [9,9,4],
  [6,6,8],
  [2,1,1]
] ))
