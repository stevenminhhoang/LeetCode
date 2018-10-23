import collections
def can_teamA_beat_teamB(matches, teamA, teamB):
    def build_graph():
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match[0]].add(match[1])
        return graph

    def dfs(graph, curr, end, visited):
        if curr == end:
            return True
        if curr in visited or curr not in graph:
            return False

        visited.add(curr)
        for team in graph[curr]:
            if dfs(graph, team, end, visited):
                return True



    graph = build_graph()
    visited = set()
    return dfs(graph, teamA, teamB, visited)
