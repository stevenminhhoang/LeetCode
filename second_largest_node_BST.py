class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def largest_node_BST(root):
    while root:
        if not root.right:
            return root.val

        root = root.right


def second_largest_node_BST(root):
    if root is None or (root.left is None and root.right is None):
        return None

    curr = root
    while curr:
        if curr.left and not curr.right:
            return largest_node_BST(curr.left)

        if curr.right and (not curr.right.left and not curr.right.right):
            return curr.val

        curr = curr.right

A = TreeNode(5)
C = TreeNode(6)
D = TreeNode(9)
E = TreeNode(12)
F = TreeNode(10)
G = TreeNode(8)
H = TreeNode(11)

A.right = C
C.right = D
D.right = E
E.left = F
F.left = G
F.right = H
print(largest_node_BST(A))
# print(second_largest_node_BST(A))
