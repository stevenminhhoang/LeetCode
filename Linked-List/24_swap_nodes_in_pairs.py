def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            first.next = second.next
            curr.next = second
            curr.next.next = first
            curr = curr.next.next

        return dummy.next
