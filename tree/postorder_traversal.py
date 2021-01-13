class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []

        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                self.res.append(node.val)
        dfs(root)
        return self.res
