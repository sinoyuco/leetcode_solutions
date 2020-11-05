class Solution:
    def findTilt(self, root: TreeNode) -> int:
        su = 0

        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            left, right = dfs(node.left), dfs(node.right)
            nonlocal su
            su += abs(left-right)
            return node.val + left + right
        dfs(root)
        return su
