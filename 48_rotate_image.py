# Clockwise
def rotate_clockwise(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        print(row)

# Anticlockwise
def rotate_anticlockwise(matrix):
    for row in matrix:
        row.reverse()
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        print(row)


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

# rotate_clockwise(matrix)
rotate_anticlockwise(matrix)
