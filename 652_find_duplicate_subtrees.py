# O(n)
def findDuplicateSubtrees(self, root):
    count = collections.Counter()
    res = []
    def dfs(node):
        if not node:
            return "#"

        # path = str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right)
        serial = "{},{},{}".format(node.val, dfs(node.left), dfs(node.right))
        count[serial] += 1
        if count[serial] == 2:
            res.append(node)

        return serial

    dfs(root)
    return res
