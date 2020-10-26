class Solution:
    def distributeCoins(self, root: TreeNode) -> int:

        result = 0

        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            nonlocal result
            result += abs(l) + abs(r)
            return node.val + l + r - 1

        dfs(root)
        return result
