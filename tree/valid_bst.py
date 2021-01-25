import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # arr = []

        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # for i in range(len(arr)-1):
        #     if arr[i]>arr[i+1]:
        #         return False
        # return True

        # def dfs(node, lower, upper):
        #     if not node:
        #         return True
        #     if node.val <= lower or node.val >= upper:
        #         return False

        #     if not dfs(node.right, node.val, upper):
        #         return False
        #     if not dfs(node.left, lower, node.val):
        #         return False
        #     return True

        # return dfs(root, -math.inf, math.inf)

        def dfs(node, l, r):
        if not node:
            return True
        if node.data <= l or node.data >= r:
            return False
        recl, recr = dfs(node.left, l, node.data), dfs(
            node.right, node.data, r)
        return recl and recr

        return dfs(root, -math.inf, math.inf)
