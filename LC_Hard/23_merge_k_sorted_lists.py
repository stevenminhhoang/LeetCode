# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# O(n * log(n))
def mergeKLists(self, lists):
    curr = head = ListNode(0)
    nodes = []
    for llist in lists:
        while llist:
            nodes.append(llist.val)
            llist = llist.next

    for x in sorted(nodes):
        curr.next = ListNode(x)
        curr = curr.next

    return head.next

# O(n * log(k))
def mergeKLists(self, lists):
    curr = head = ListNode(0)
    heap = []
    for l in lists:
        if l:
            heapq.heappush(heap, (l.val, l))

    while heap:
        curr.next = heapq.heappop(heap)[1]
        curr = curr.next
        if curr.next:
            heapq.heappush(heap, (curr.next.val, curr.next))

    return head.next
