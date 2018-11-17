# O(E + E*log(E)) E is number of edges
import collections, heapq
def network_delay_time(times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    distance = {}
    heap = []
    heap.append((0, K))
    while heap:
        d, node = heapq.heappop(heap)
        if node in distance:
            continue
        distance[node] = d
        for nei, d2 in graph[node]:
            if nei not in distance:
                heapq.heappush(heap, (d + d2, nei))

    ans = max(distance.values())
    return ans if len(distance) == N else -1


print(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
