class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.maps = {}

        def dfs(node):
            if not node:
                return False
            if node.val in self.maps:
                return True
            self.maps[k-node.val] = 1
            l, r = dfs(node.left), dfs(node.right)
            return l or r

        return dfs(root)
