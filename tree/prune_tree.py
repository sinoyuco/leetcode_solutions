class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return False
            l, r = dfs(node.left), dfs(node.right)
            if not l:
                node.left = None
            if not r:
                node.right = None
            return node.val == 1 or l or r

        if dfs(root):
            return root
        else:
            return None
