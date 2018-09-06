# O(m * n)
def spiral_matrix(matrix):
    if not matrix:
        return []

    res = []
    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1
    while row_begin <= row_end and col_begin <= col_end:
        # Traverse right
        for i in range(col_begin, col_end + 1):
            res.append(matrix[row_begin][i])

        row_begin += 1
        # Traverse down
        for i in range(row_begin, row_end + 1):
            res.append(matrix[i][col_end])

        col_end -= 1
        # Traverse left
        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                res.append(matrix[row_end][i])

        row_end -= 1
        if col_begin <= col_end:
        # Traverse up
            for i in range(row_end, row_begin - 1, -1):
                res.append(matrix[i][col_begin])

        col_begin += 1

    return res


grid = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

print(spiral_matrix(grid))
