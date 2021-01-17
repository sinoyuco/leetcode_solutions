import collections


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        self.maps = defaultdict(list)
        self.mi = 0
        self.ma = 0

        def dfs(node, w, d):
            if not node:
                return
            self.maps[w] += [(d, node.val)]
            self.mi = min(self.mi, w)
            self.ma = max(self.ma, w)
            dfs(node.left, w-1, d+1)
            dfs(node.right, w+1, d+1)

        dfs(root, 0, 0)
        res = []
        for i in range(self.mi, self.ma+1):
            res.append([val for row, val in sorted(self.maps[i])])
        return res
