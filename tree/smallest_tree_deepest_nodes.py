class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return (0, None)
            l,llca = dfs(node.left)
            r, rlca = dfs(node.right)
            
            if l > r:
                return (l+1, llca)
            if r > l:
                return (r+1, rlca)
            return (l+1, node)
                
        return dfs(root)[1]