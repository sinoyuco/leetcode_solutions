class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        curr, d = head, ListNode(-1)
        while curr:
            temp, p, n = curr.next, d, d.next
            while n:
                if n.val >= curr.val:
                    break
                p = n
                n = n.next
            curr.next = n
            p.next = curr
            curr = temp
        return d.next
