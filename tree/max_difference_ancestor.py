import math


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxval = 0

        def dfs(node, maxv, minv):
            if not node:
                return
            nonlocal maxval
            maxval = max(maxval, abs(maxv-node.val), abs(minv-node.val))

            if node.val < minv:
                minv = node.val
            if node.val > maxv:
                maxv = node.val
            dfs(node.left, maxv, minv)
            dfs(node.right, maxv, minv)

        dfs(root, root.val, root.val)
        return maxval
        
