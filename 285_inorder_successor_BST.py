def inorder_successor_BST(root, p):
    prev = None
    while root:
        if p.val < root.val:
            prev = root
            root = root.left
        else:
            root = root.right

    return prev
