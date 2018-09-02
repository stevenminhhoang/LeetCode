# O(N + E), where N is the number of rooms, and E is the total number of keys.

# BFS
def canVisitAllRooms(rooms):
    visited = set()
    queue = collections.deque()
    queue.append(rooms[0])
    visited.add(0)
    while queue:
        curr = queue.popleft()
        for i in curr:
            if i not in visited:
                visited.add(i)
                queue.append(rooms[i])

    return len(visited) == len(rooms)

# DFS
def canVisitAllRooms(rooms):
    def dfs(id, visited, rooms):
        if id in visited:
            return
        visited.add(id)
        for keys in rooms[id]:
            dfs(keys, visited, rooms)

    visited = set()
    dfs(0, visited, rooms)
    return len(visited) == len(rooms)
