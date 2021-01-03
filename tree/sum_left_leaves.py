class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self.s = 0
        
        def dfs(node, goneLeft):
            if not node:
                return
            if goneLeft and (not node.left and not node.right):
                self.s += node.val
            dfs(node.left, True)
            dfs(node.right, False)
            
        dfs(root, False)
        return self.s