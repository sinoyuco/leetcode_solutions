class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return (0,0)
            l,r = dfs(node.left), dfs(node.right)
            r, skip = node.val + l[1] + r[1], max(l)+max(r)
            return (r,skip)
        return max(dfs(root))