# O(n * log(n))
def sortedListToBST(self, head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    if not head:
        return None

    if not head.next:
        return TreeNode(head.val)

    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None
    root = TreeNode(slow.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(slow.next)

    return root

# O(n)
def sortedListToBST(self, head):
    def inorder(start, end):
        if start > end:
            return None

        mid = start + (end - start) // 2
        left = inorder(start, mid - 1)
        root = TreeNode(self.node.val)
        root.left = left
        self.node = self.node.next
        right = inorder(mid + 1, end)
        root.right = right

        return root


    if not head:
        return

    size = 0
    curr = head
    self.node = head
    while curr:
        curr = curr.next
        size += 1

    return inorder(0, size - 1)
