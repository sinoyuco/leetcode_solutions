class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def dfs(node, s):
            if not node:
                return False
            if not node.left and not node.right:
                return node.val+s == sum
            return dfs(node.left, s+node.val) or dfs(node.right, s+node.val)

        return dfs(root, 0)
