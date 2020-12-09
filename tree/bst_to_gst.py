class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0

        def dfs(node):
            if not node:
                return
            dfs(node.right)
            nonlocal s
            n = node.val
            node.val += s
            s += n
            dfs(node.left)
            return node
        return dfs(root)
