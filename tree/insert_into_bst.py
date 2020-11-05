class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return TreeNode(val)

        def dfs(node):
            if not node:
                return
            a = TreeNode(val)
            if val > node.val:
                if node.right:
                    dfs(node.right)
                else:
                    node.right = a
            else:
                if node.left:
                    dfs(node.left)
                else:
                    node.left = a
        dfs(root)
        return root
