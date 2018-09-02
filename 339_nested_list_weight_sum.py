# O(n)
def depthSum(self, nestedList):
    def dfs(lis, depth):
        s = 0
        for n in lis:
            if n.isInteger():
                s += n.getInteger() * depth
            else:
                s += dfs(n.getList(), depth + 1)

        return s

    return dfs(nestedList, 1)
