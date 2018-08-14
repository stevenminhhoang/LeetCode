def same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)
