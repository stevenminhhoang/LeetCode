# O(m * n)
import collections
# BFS
# def flood_fill(image, sr, sc, newColor):
#     color = image[sr][sc]
#     if color == newColor:
#         return image
#
#     queue = collections.deque()
#     queue.append((sr, sc))
#     image[sr][sc] = newColor
#     while queue:
#         row, col = queue.popleft()
#         image[row][col] = newColor
#         for dir in [(1,0), (0,1), (-1,0), (0,-1)]:
#             nr, nc = row + dir[0], col + dir[1]
#             if not (0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == color):
#                 continue
#             queue.append((nr, nc))
#
#     return image
#
# print(flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

def flood_fill(image, sr, sc, newColor):
    def dfs(image, row, col, color, newColor):
        if not (0 <= row < len(image) and 0 <= col < len(image[0])):
            return
        if image[row][col] != color:
            return

        image[row][col] = newColor
        dfs(image, row - 1, col, color, newColor)
        dfs(image, row + 1, col, color, newColor)
        dfs(image, row, col - 1, color, newColor)
        dfs(image, row, col + 1, color, newColor)

    color = image[sr][sc]
    if color == newColor:
        return image

    dfs(image, sr, sc, color, newColor)
    return image

print(flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
