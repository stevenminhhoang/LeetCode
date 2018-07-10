def transpose_matrix(A):
    B = [[0 for i in range(len(A))] for j in range(len(A[0]))]
    for row in range(len(A)):
        for col in range(len(A[0])):
            B[col][row] = A[row][col]

    return B

print(transpose_matrix([[1,2,3],[4,5,6],[7,8,9]]))
