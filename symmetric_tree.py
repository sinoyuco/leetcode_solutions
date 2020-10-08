class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def dfs(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return (n1.val == n2.val) and dfs(n1.right, n2.left) and dfs(n1.left, n2.right)

        return dfs(root, root)
