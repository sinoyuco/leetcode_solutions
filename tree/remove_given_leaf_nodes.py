class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        
        def dfs(node):
            if not node:
                return None
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)
            if not node.left and not node.right and node.val == target:
                return None
            return node
        
        return dfs(root)