"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emap = {e.id: e for e in employees}
        def dfs(e_id):
            employee = emap[e_id]
            return (employee.importance + sum(dfs(sub_id) for sub_id in employee.subordinates))

        return dfs(id)

# BFS
def getImportance(self, employees, id):
    dic = {}
    ans = 0
    for employee in employees:
        dic[employee.id] = employee
    queue = collections.deque()
    queue.append(dic[id])
    while queue:
        curr = queue.popleft()
        ans += curr.importance
        for subordinate in curr.subordinates:
            queue.append(dic[subordinate])

    return ans
