class Solution:
    def tree2str(self, t: TreeNode) -> str:
        
        def dfs(node):
            if not node:
                return ''
            if not node.left and not node.right:
                return str(node.val)
            if node.left and not node.right:
                return str(node.val) + '('+ dfs(node.left) +')'
            if node.right and not node.left:
                return str(node.val) + '()'+'('+ dfs(node.right) +')'
            return str(node.val) + '('+ dfs(node.left) +')' + '('+ dfs(node.right) +')'
        return dfs(t)