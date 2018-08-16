# O(n * log(n) if balanced tree or O(n^2) if skewed tree)
def buildTree(self, preorder, inorder):
    def create_tree(pre_start, in_start, in_end, preorder, inorder):
        if pre_start > len(preorder) - 1 or in_start > in_end:
            return
        root = TreeNode(preorder[pre_start])
        inorder_root_index = 0
        for i in range(in_start, in_end + 1):
            if inorder[i] == root.val:
                inorder_root_index = i

        root.left = create_tree(pre_start + 1, in_start, inorder_root_index - 1, preorder, inorder)
        root.right = create_tree(pre_start + inorder_root_index - in_start + 1, inorder_root_index + 1, in_end, preorder, inorder)

        return root

    return create_tree(0, 0, len(inorder) - 1, preorder, inorder)

# O(n)
def buildTree(self, preorder, inorder):
    def create_tree(pre_start, in_start, in_end, preorder, inorder, inmap):
        if pre_start > len(preorder) - 1 or in_start > in_end:
            return
        root = TreeNode(preorder[pre_start])
        inorder_root_index = inmap[root.val]

        root.left = create_tree(pre_start + 1, in_start, inorder_root_index - 1, preorder, inorder, inmap)
        root.right = create_tree(pre_start + inorder_root_index - in_start + 1, inorder_root_index + 1, in_end, preorder, inorder, inmap)

        return root

    inmap = {}
    for i in range(len(inorder)):
        inmap[inorder[i]] = i

    return create_tree(0, 0, len(inorder) - 1, preorder, inorder, inmap)
