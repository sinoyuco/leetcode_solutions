class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)

        dfs(root)
        minv = math.inf
        for i in range(1, len(self.arr)):
            minv = min(minv, self.arr[i]-self.arr[i-1])
        return minv
