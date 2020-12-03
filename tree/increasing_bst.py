class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        res = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
            
        dfs(root)
        a = TreeNode(res.pop(0))
        p = a
        while res:
            n = TreeNode(res.pop(0))
            a.right = n
            a = a.right
        return p