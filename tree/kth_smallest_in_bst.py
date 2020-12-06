class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
        dfs(root)
        return res[k-1]
