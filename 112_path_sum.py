# Recursive
def hasPathSum(self, root, sum):
    def pathSumFrom(node, sum):
        if not node:
            return False

        if not node.left and not node.right and sum - node.val == 0:
            return True

        return pathSumFrom(node.left, sum - node.val) or pathSumFrom(node.right, sum - node.val)

    return pathSumFrom(root, sum)


# Iterative
def hasPathSum(self, root, sum):
    if not root:
        return False
    stack = []
    stack_val = []
    stack.append(root)
    stack_val.append(root.val)
    while stack:
        node = stack.pop()
        val = stack_val.pop()
        if not node.left and not node.right and val == sum:
            return True
        else:
            if node.right:
                stack.append(node.right)
                stack_val.append(node.right.val + val)
            if node.left:
                stack.append(node.left)
                stack_val.append(node.left.val + val)

    return False
