def get_row(rowIndex):
    # Method 1
    # ans = [0] * (rowIndex + 1)
    # ans[0] = 1
    # for i in range(1, rowIndex + 1):
    #     for j in range(i, 0, -1):
    #         ans[j] += ans[j-1]
    #
    # return ans

    # Method 2
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x,y in zip([0] + row, row + [0])]

    return row




print(get_row(5))
