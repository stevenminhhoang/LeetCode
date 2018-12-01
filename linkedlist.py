class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    curr = head = ListNode(-1)
    while l1 and l2:
        curr.next = l1
        l1 = l1.next
        curr = curr.next
        curr.next = l2
        l2 = l2.next
        curr = curr.next


    if l1:
        curr.next = l1
    if l2:
        curr.next = l2

    return head.next

a = ListNode(1)
b = ListNode(3)
c = ListNode(4)
d = ListNode(2)
# e = ListNode(4)
# f = ListNode(6)
a.next = b
b.next = c

# d.next = e
# e.next = f

head = mergeTwoLists(a, d)
while head:
    print(head.val)
    head = head.next
