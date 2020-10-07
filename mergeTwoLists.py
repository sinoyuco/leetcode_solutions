class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        d = ListNode()
        c = d
        while l1 and l2:
            if l1.val < l2.val:
                c.next = l1
                l1 = l1.next
            else:
                c.next = l2
                l2 = l2.next
            c = c.next

        #at this point, even if multiples nodes are left at list1 or list2, you can mass link up the rest.
        if l1:
            c.next = l1
        elif l2:
            c.next = l2
        return d.next
