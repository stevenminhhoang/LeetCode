import collections, heapq
def dijkstra(n, flights, src, dst, k):
    distance = collections.defaultdict(dict)
    for u, v, w in flights:
        distance[u][v] = w

    heap = [(0, src, k + 1)]
    while heap:
        d, node, k = heapq.heappop(heap)
        if node == dst:
            return d

        if k > 0:
            for nei in distance[node]:
                heapq.heappush(heap, (d + distance[node][nei], nei, k - 1))

    return -1

print(dijkstra(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
