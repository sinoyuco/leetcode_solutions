class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            r, l = self.invertTree(root.right), self.invertTree(root.left)
            root.left, root.right = r, l
            return root
