class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sumval = 0

        def dfs(node, l, h):
            if node:
                nonlocal sumval
                if l <= node.val <= h:
                    sumval += node.val
                if node.val > l:
                    dfs(node.left, l, h)
                if node.val < h:
                    dfs(node.right, l, h)
                    
        dfs(root, low, high)
        return sumval
