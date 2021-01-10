class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 == root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        l = self.flipEquiv(root1.left, root2.left)
        r = self.flipEquiv(root1.right, root2.right)
        lr = self.flipEquiv(root1.left, root2.right)
        rl = self.flipEquiv(root1.right, root2.left)
        return (l and r) or (rl and lr)
