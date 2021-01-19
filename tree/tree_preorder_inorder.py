class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return
        v = postorder.pop()
        root = TreeNode(v)
        idx = inorder.index(v)

        r = self.buildTree(inorder[(idx+1)::], postorder)
        l = self.buildTree(inorder[:(idx):], postorder)

        root.right = r
        root.left = l

        return root
