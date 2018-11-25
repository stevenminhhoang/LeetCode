# BFS topological sort
import collections
def course_schedule(num_courses, prerequisites):
    graph = {x: [] for x in range(num_courses)}
    indegrees = [0] * num_courses
    queue = collections.deque()

    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegrees[pre[0]] += 1

    for i in range(num_courses):
        if indegrees[i] == 0:
            queue.append(i)

    while queue:
        course = queue.popleft()
        for nei in graph[course]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                queue.append(nei)

    for i in range(num_courses):
        if indegrees[i] != 0:
            return False

    return True

print(course_schedule(2, [[1,0]]))

# DFS to detect cycle in directed graph
def course_schedule(num_courses, prerequisites):
    def isCyclic(node, graph, visited, recStack):
        # Mark current node as visited and add to recursion stack
        visited[node] = True
        recStack[node] = True
        for nei in graph[node]:
            if not visited[nei]:
                if isCyclic(nei, graph, visited, recStack):
                    return True
            elif visited[nei] == True and recStack[nei] == True:
                return True

        # Backtrack, pop current node from recursion stack
        recStack[node] = False
        return False


    graph = collections.defaultdict(set)
    for pre in prerequisites:
        graph[pre[1]].add(pre[0])

    visited = [False] * num_courses
    onpath = [False] * num_courses
    for i in range(num_courses):
        if not visited[i]:
            if isCyclic(i, graph, visited, onpath):
                return False

    return True

print(course_schedule(2, [[1,0],[0,1]]))
