# DFS
# O(V + E)
import collections
def course_schedule_II(num_courses, prerequisites):
    def hasOrder(node, graph, visited, recStack, res):
        # Mark current node as visited and add to recursion stack
        visited[node] = True
        recStack[node] = True
        for nei in graph[node]:
            if not visited[nei]:
                if not hasOrder(nei, graph, visited, recStack, res):
                    return False
            elif recStack[nei] == True:
                return False

        recStack[node] = False
        res.append(node)
        return True

    graph = collections.defaultdict(set)
    for pre in prerequisites:
        graph[pre[1]].add(pre[0])

    visited = [False] * num_courses
    res = []
    recStack = [False] * num_courses
    for i in range(num_courses):
        if not visited[i]:
            if hasOrder(i, graph, visited, recStack, res) == False:
                return []

    return res[::-1]

print(course_schedule_II(4, [[1,0],[2,0],[3,1],[3,2]]))
