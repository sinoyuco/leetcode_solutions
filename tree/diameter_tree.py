class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        res = 0

        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            nonlocal res
            res = max(res, l+r)
            return max(l, r)+1

        dfs(root)
        return res
