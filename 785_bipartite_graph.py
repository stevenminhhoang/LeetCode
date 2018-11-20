# O(V + E)
def bipartite_graph(graph):
    def valid(color, curr, graph, colors):
        if colors[curr] != 0:
            return colors[curr] == color

        colors[curr] = color
        for nei in graph[curr]:
            if not valid(-color, nei, graph, colors):
                return False

        return True


    graph_dict = {}
    for i in range(len(graph)):
        graph_dict[i] = graph[i]

    colors = [0] * len(graph)
    for i in range(len(colors)):
        if colors[i] == 0 and not valid(1, i, graph, colors):
            return False

    return True

print(bipartite_graph([[1,3], [0,2], [1,3], [0,2]]))

# Alternative
def bipartite_graph(graph):
    def dfs(color, curr, dic, visited):
        if visited[curr] != 0:
            return visited[curr] == color

        visited[curr] = color
        for nei in dic[curr]:
            if not dfs(-color, nei, dic, visited):
                return False

        return True

    graph_dict = {}
    for i in range(len(graph)):
        graph_dict[i] = graph[i]

    visited = {}
    for i in range(len(graph)):
        visited[i] = 0

    for i in range(len(visited)):
        if visited[i] == 0 and not dfs(1, i, graph_dict, visited):
            return False

    return True
