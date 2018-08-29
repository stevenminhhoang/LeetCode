# O(N + E), where N is the number of rooms, and E is the total number of keys.
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
