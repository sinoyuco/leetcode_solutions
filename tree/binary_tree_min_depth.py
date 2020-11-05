class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def dfs(node):
            if not node:
                return 0

            if node.right is not None and node.left is None:
                return 1+dfs(node.right)
            if node.left is not None and node.right is None:
                return 1+dfs(node.left)
            else:
                return 1+min(dfs(node.left), dfs(node.right))

        return dfs(root)
