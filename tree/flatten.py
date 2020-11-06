class Solution:
    def flatten(self, root: TreeNode) -> None:
        
        def dfs(node):
            if not node:
                return None
            l, r = dfs(node.left), dfs(node.right)
            if l:
                node.right = l
                while l.right:
                    l = l.right
                l.right = r
            else:
                node.right = r
            node.left = None
            return node
        dfs(root)
