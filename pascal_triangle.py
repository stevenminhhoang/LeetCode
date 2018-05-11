def pascal_triangle(numRows):
    ans = [[1] * (x + 1) for x in range(numRows)]

    for i in range(2, numRows):
        for j in range(1, i):
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j]

    # return ans
    for i in range(len(ans)):
        print(ans[i])

pascal_triangle(10)
