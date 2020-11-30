class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def dfs(node):
            if not node:
                return False
            l, r = dfs(node.left), dfs(node.right)
            m = (node == p) or (node == q)
            if m+l+r >= 2:
                nonlocal res
                res = node
            return m or l or r
            
        dfs(root)
        return res
