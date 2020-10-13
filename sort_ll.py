class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        # get all values from the linked list and append to an empty list
        if not head:
            return None
        b = head
        vals = []
        while b:
            vals.append(b.val)
            b = b.next

        #sort the list
        vals.sort()
        l = a = ListNode(vals[0])
        # create a new listnodes at every step and construct the linked list.
        for i in range(1, len(vals)):
            a.next = ListNode(vals[i])
            a = a.next
        return l

        # Although this solution uses O(n) time complexity, it also uses O(n) space complexity,
        # and therefore is not optimal.