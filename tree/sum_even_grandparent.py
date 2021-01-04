class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        def dfs(node, p, g):
            if not node:
                return 0
            tot = 0
            if g and g.val % 2 == 0:
                tot += node.val
            return tot + dfs(node.left, node, p) + dfs(node.right, node, p)
        
        return dfs(root, None, None)