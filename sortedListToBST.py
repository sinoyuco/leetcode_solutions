class Solution:
    def listTraversal(self, head):
         slow = fast = head
          prev = None
           while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        top = self.listTraversal(head)

        node = TreeNode(top.val)

        if head == top:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(top.next)
        return node
