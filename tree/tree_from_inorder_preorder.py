class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) > 0:
            root = TreeNode(preorder[0])
            idx = inorder.index(root.val)

            lin, rin = inorder[idx:], inorder[(idx+1):]
            lpre = preorder[1:(1+len(lin))]
            rpre = preorder[(1+len(lin)):]


            l = self.buildTree(lpre, lin)
            r = self.buildTree(rpre, rin)

            root.left, root.right = l,r

            return root
        return None
