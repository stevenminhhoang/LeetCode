def edges(rows, cols):
    total = (rows - 1) * cols + rows * (cols - 1)
    return total

print(edges(3, 4))
