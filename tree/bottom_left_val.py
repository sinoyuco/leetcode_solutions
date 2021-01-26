import collections
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        if not root:
            return None

        queue = [root]
        res = []
        while queue:
            l, t = len(queue), []
            while l > 0:
                c = queue.pop(0)
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
                t.append(c.val)
                l -= 1
            res.append(t)
        return res[-1][0]

        # self.maxval = -math.inf
        # self.res = -1

        # def dfs(node, d):
        #     if not node:
        #         return
        #     if d > self.maxval:
        #         self.maxval = d
        #         self.res = node.val
        #     dfs(node.left, d+1)
        #     dfs(node.right, d+1)

        # dfs(root, 0)
        # return self.res
