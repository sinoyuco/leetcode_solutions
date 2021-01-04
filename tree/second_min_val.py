class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.s = set()
        def dfs(node):
            if node:
                self.s.add(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        p = list(self.s)

        t, m = math.inf, min(p)
        for i in p:
            if i != m and i < t:
                t = i
        return t if t != math.inf else -1
