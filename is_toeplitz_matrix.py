def is_toeplitz_matrix(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r-1):
        for j in range(c-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False

    return True


is_toeplitz_matrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
