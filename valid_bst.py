class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr == sorted(list(set(arr)))
