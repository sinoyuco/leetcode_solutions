class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val > root.val:
            n = TreeNode(val, root, None)
            return n
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
        return root
