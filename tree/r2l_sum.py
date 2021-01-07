class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.sum = 0
        
        def dfs(node, path):
            if node:
                if not node.left and not node.right:
                    n = ''.join([str(i) for i in path+[node.val]])
                    self.sum += int(n)
                    return
                dfs(node.left, path+[node.val])
                dfs(node.right, path+[node.val])
            
        dfs(root, [])
        
        return self.sum