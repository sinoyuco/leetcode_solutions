class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        if not head.next or k == 0:
            return head

        llen = 1
        slow = fast = head
        while fast.next:
            fast = fast.next
            llen += 1
        print(llen)
        fast = head

        if k % llen == 0:
            return head

        for i in range(k % llen):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        newhead = slow.next
        slow.next = None
        fast.next = head
        return newhead
