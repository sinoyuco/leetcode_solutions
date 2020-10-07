class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        def reverseList(node):
            c = node
            p = None
            while c:
                n = c.next
                c.next = p
                p = c
                c = n
            return p

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        fast = head
        slow = reverseList(slow)
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
