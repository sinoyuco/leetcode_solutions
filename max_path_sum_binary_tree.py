import math


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_val = -math.inf

        def dfs(node):
            if not node:
                return 0

            lsum, rsum = dfs(node.left), dfs(node.right)

            bothsides, oneside = node.val+lsum+rsum, node.val+max(lsum, rsum)
            nonlocal max_val
            max_val = max(max_val, bothsides)
            return max(0, oneside)

        dfs(root)
        return max_val
