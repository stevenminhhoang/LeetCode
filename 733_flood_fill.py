def flood_fill(image, sr, sc, newColor):
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return image
    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r > 0:
                dfs(r-1, c)
            if r < R - 1:
                dfs(r+1, c)
            if c > 0:
                dfs(r, c-1)
            if c < C - 1:
                dfs(r, c+1)
    dfs(sr, sc)

    return image

print(flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
