class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
          a, b = headA, headB
           # while they are not equal, pointers keep becoming the next.
           # if they reach the end of the list, they start at the opposing side.
           # after both start at the opposing side, if there is an intersection, they will meet there.
           # if not, both will be null at the same time and equal, and null will be returned.
           while a != b:
                if a:
                    a = a.next
                else:
                    a = headB

                if b:
                    b = b.next
                else:
                    b = headA
            return a
