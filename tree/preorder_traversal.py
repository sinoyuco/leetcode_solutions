class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []

        def dfs(node):
            if node:
                self.res.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.res
