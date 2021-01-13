class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        self.seen = {}
        self.res = []

        def dfs(node):
            if not node:
                return ''
            l, r = dfs(node.left), dfs(node.right)
            c = str(node.val)+'-'+l+'-'+r
            if c not in self.seen:
                self.seen[c] = 1
            else:
                self.seen[c] += 1

            if self.seen[c] == 2:
                self.res.append(node)
            return c
        dfs(root)
        return self.res
