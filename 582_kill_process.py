# O(n)
# DFS
import collections
def kill_process(pid, ppid, kill):
    def dfs(res, dic, kill):
        res.append(kill)
        for id in dic[kill]:
            dfs(res, dic, id)

    dic = collections.defaultdict(list)
    for i in range(len(ppid)):
        if ppid[i] > 0:
            dic[ppid[i]].append(pid[i])

    ans = []
    # ans.append(kill)
    dfs(ans, dic, kill)
    return ans

print(kill_process([1, 3, 10, 5], [3, 0, 5, 3], 5))

# BFS
def killProcess(pid, ppid, kill):
    dic = collections.defaultdict(list)
    for i in range(len(ppid)):
        if ppid[i] > 0:
            dic[ppid[i]].append(pid[i])

    queue = collections.deque()
    queue.append(kill)
    ans = []
    while queue:
        node = queue.popleft()
        ans.append(node)
        for id in dic[node]:
            queue.append(id)

    return ans
