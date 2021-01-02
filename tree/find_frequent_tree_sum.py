import collections
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.maps = collections.defaultdict(int)

        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            c = node.val + l + r
            self.maps[c] += 1
            return c

        dfs(root)
        m = max(self.maps.values())
        arr = []
        for k, v in self.maps.items():
            if v == m:
                arr.append(k)
        return arr
