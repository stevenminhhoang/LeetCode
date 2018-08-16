def buildTree(self, inorder, postorder):
    def create_tree(post_start, in_start, in_end, inorder, postorder, inmap):
        if post_start < 0 or in_start > in_end:
            return
        root = TreeNode(postorder[post_start])
        ir_index = inmap[root.val]

        root.right = create_tree(post_start - 1, ir_index + 1, in_end, inorder, postorder, inmap)
        root.left = create_tree(post_start - (in_end - ir_index) - 1, in_start, ir_index - 1, inorder, postorder, inmap)

        return root

    inmap = {}
    for i in range(len(inorder)):
        inmap[inorder[i]] = i

    root = create_tree(len(postorder) - 1, 0, len(inorder) - 1, inorder, postorder, inmap)
    return root
