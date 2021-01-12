class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return None

        self.res = []
        l = set(to_delete)

        def dfs(node):
            if not node:
                return None
            if node:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
            if node.val in l:
                self.res.extend([node.left, node.right])
                node = None
            return node

        self.res.append(dfs(root))
        print(self.res)
        return [i for i in self.res if i]
