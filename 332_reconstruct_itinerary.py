# O(n * log(n))
import collections, heapq
def reconstruct_itinerary(tickets):
    def dfs(graph, node, path):
        arrivals = graph[node]
        while arrivals:
            dfs(graph, heapq.heappop(arrivals), path)

        path.append(node)
        return path[::-1]

    graph = collections.defaultdict(list)
    for ticket in tickets:
        heapq.heappush(graph[ticket[0]], ticket[1])

    return dfs(graph, "JFK", [])

print(reconstruct_itinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
