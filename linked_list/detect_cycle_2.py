class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # O(n) space complexity
        # l = set()
        # n = head
        # while n:
        #     if n in l:
        #         return n
        #     else:
        #         l.add(n)
        #     n=n.next
        # return None

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
