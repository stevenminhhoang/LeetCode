# O(h) or O(log(n)) h is height of tree
def findMin(self, node):
    while node.left:
        node = node.left

    return node

def deleteNode(self, root, key):
    if not root:
        return
    if root.val > key:
        root.left = self.deleteNode(root.left, key)
    elif root.val < key:
        root.right = self.deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        min_node = self.findMin(root.right)
        root.val = min_node.val
        root.right = self.deleteNode(root.right, root.val)

    return root
