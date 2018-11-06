def range_addition_II(m, n, ops):
    if not ops:
        return m * n

    min_row = float('inf')
    min_col = float('inf')
    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])

    return min_row * min_col

print(range_addition_II(3, 3, [[2,2],[3,3]]))
