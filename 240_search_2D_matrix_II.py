# O(n + m)
def search_matrix(matrix, target):
    if not matrix or target is None:
        return False

    row, col = 0, len(matrix[0]) - 1
    while col >= 0 and row < len(matrix):
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1

    return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(search_matrix(matrix, 16))
