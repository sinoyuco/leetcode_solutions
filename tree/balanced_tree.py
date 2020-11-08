class Solution:
    def height(self, root):
        if not root:
            return 0
        l, r = self.height(root.left), self.height(root.right)
        if l == -1 or r == -1 or abs(l-r) > 1:
            return -1
        return 1+max(l, r)

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return False if self.height(root) == -1 else True
