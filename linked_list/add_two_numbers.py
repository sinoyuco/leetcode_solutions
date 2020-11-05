class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = s2 = ''
        a, b = l1, l2
        while a or b:
            if a:
                s1 += str(a.val)
                a = a.next
            if b:
                s2 += str(b.val)
                b = b.next
        new_s = str(int(s1[::-1])+int(s2[::-1]))[::-1]
        print(new_s)
        if len(new_s) == 0:
            return None

        p = newhead = ListNode(new_s[0])
        for i in range(1, len(new_s)):
            nextnode = ListNode(new_s[i])
            newhead.next = nextnode
            newhead = newhead.next
        return p
