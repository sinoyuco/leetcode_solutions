class Solution:
    def TreeSize(self, node):
        if not node:
            return 0
        return 1 + self.TreeSize(node.left) + self.TreeSize(node.right)

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        if not root:
            return False
        if root.val == x:
            l, r = self.TreeSize(root.left), self.TreeSize(root.right)
            s = l + r + 1
            if l > n-l or r > n-r or s < n-s:
                return True
            return False
        return self.btreeGameWinningMove(root.left, n, x) or self.btreeGameWinningMove(root.right, n, x)
