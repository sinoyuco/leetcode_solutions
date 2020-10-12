class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        def dfs(node, value):
            if node:
                if node.val == value:
                    return node
                elif value < node.val:
                    return dfs(node.left, value)
                else:
                    return dfs(node.right, value)

        return dfs(root, val)
