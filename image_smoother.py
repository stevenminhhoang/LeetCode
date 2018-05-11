def image_smoother(M):
    row, col = len(M), len(M[0])
    ans = [[0] * col for _ in M ]
    for r in range(row):
        for c in range(col):
            count = 0
            nsum = 0
            for nr in (r-1, r, r+1):
                for nc in (c-1, c, c+1):
                    if 0 <= nr < row and 0 <= nc < col:
                        count += 1
                        nsum += M[nr][nc]
            nsum //= count
            ans[r][c] = nsum

    return ans




print(image_smoother([[1,1,1],
 [1,0,1],
 [1,1,1]]))
