# O(log(n))
# Iterative
def insertIntoBST(self, root, val):
        prev = None
        curr = root
        while curr:
            prev = curr
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        if prev:
            if prev.val < val:
                prev.right = TreeNode(val)
            else:
                prev.left = TreeNode(val)
        else:
            root = TreeNode(val)

        return root

# Recursive
def insertIntoBST(self, root, val):
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = self.insertIntoBST(root.right, val)
    else:
        root.left = self.insertIntoBST(root.left, val)

    return root
