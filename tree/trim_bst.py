class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            if node.val > high:
                return dfs(node.left)
            elif node.val < low:
                return dfs(node.right)
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
        return dfs(root)