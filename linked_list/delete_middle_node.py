class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_middle_node(head):
    fast = slow = head
    p = None
    while fast and fast.next:
        fast = fast.next.next
        p = slow
        slow = slow.next
    p.next = slow.next

    # curr,res = head, []
    # while curr:
    #     res.append(curr.val)
    #     curr = curr.next
    # print(res)

    return head


e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

print(delete_middle_node(a))
