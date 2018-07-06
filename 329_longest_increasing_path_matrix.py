def longest_increasing_path(matrix):
    ans = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0]):
            ans = max(ans, dfs(matrix, row, col))

    return ans

def dfs(matrix, row, col):
    if not (0 <= row < len(matrix) and )
