class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        head = p = ListNode(0)
        for n in sorted(nodes):
            p.next = ListNode(n)
            p = p.next
        return head.next
