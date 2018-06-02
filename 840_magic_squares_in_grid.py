def magic(a,b,c,d,e,f,g,h,i):
    return (sorted([a,b,c,d,e,f,g,h,i]) == range(1, 10) and a+b+c == d+e+f == g+h+i == a+d+g == b+e+h
            == c+f+i == a+e+i == c+e+g)


def magic_squares_in_grid(grid):
    count = 0
    R, C = len(grid), len(grid[0])
    for i in range(R - 2):
        for j in range(C - 2):
            if magic(grid[i][j],grid[i][j+1],grid[i][j+2],grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]):
                count += 1

    return count

print(magic_squares_in_grid([[4,3,8,4], [9,5,1,9], [2,7,6,2]]))
