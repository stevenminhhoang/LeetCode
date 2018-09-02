import collections
def course_schedule(num_courses, prerequisites):
    graph = {i: set() for i in range(num_courses)}
    in_degree = {i: 0 for i in range(num_courses)}

    for pre in prerequisites:
        graph[pre[1]].add(pre[0])
        in_degree[pre[0]] += 1


    queue = collections.deque()
    topology = []
    for i, degree in in_degree.items():
        if degree == 0:
            queue.append(i)

    while queue:
        course = queue.popleft()
        topology.append(course)
        for n in graph[course]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)

    return count == num_courses


print(course_schedule(2, [[1,0]] ))
