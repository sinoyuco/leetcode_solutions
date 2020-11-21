class Solution:
    def dfs(self, root, head):
        if head and not root:
            return False
        if not head:
            return True
        if head.val != root.val:
            return False
        return self.dfs(root.left, head.next) or self.dfs(root.right, head.next)
        
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        if not head:
            return True
        if root.val != head.val:
            return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        else:
            if self.dfs(root,head):
                return True
            else:
                return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)