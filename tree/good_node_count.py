class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root: return 0
        self.count = 0
        
        def dfs(node, m):
            if not node:
                return
            if node.val >= m:
                self.count+=1
            m = max(m, node.val)
            dfs(node.left,m)
            dfs(node.right,m)
            
        dfs(root, root.val)
        return self.count