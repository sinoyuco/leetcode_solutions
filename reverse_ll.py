class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        c = head
        p = None
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        return p
