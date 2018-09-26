# O(m * n)
def lonely_pixel(picture):
    rows = [0] * len(picture)
    cols = [0] * len(picture[0])
    res = 0
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if picture[i][j] == 'B':
                rows[i] += 1
                cols[j] += 1

    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1:
                res += 1

    return res


print(lonely_pixel([['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]))
