class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.m = 0
        def dfs(node):
            if not node:
                return 0
            l,r = dfs(node.left), dfs(node.right)
            lpath = rpath = 0
            if node.left and node.left.val == node.val:
                lpath = l+1
            if node.right and node.right.val == node.val:
                rpath = r+1
            self.m = max(self.m, lpath+rpath)
            return max(lpath,rpath)
        
        dfs(root)
        return self.m