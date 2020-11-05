class Solution:
    # def reverse(self, startNode, endNode):
    #     curr = startNode
    #     prev = endNode.next
    #     while curr:
    #         n = curr.next
    #         curr.next = prev
    #         prev = curr
    #         c = n
    #     return p

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        ahead, behind = head, None

        while m > 1:
            behind = ahead
            ahead = ahead.next
            m -= 1
            n -= 1
        print(behind.val, ahead.val)

        c, t = behind, ahead

        while n > 0:
            nextn = ahead.next
            ahead.next = behind
            behind = ahead
            ahead = nextn
            n -= 1

        print(behind.val, ahead.val)

        if c:
            c.next = behind
        else:
            head = behind
        t.next = ahead
        return head
