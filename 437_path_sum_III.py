# O(n * 2)
def pathSum(self, root, sum):
    def pathSumFrom(node, sum):
        if not node:
            return 0

        return int(node.val == sum) + pathSumFrom(node.left, sum - node.val) + pathSumFrom(node.right, sum - node.val)

    if not root:
        return 0

    return pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

# O(N)
def pathSum(self, root, sum):
    
