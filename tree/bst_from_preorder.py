class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = None
        for c in preorder:
            if not root:
                root = TreeNode(c)
            else:
                t = root
                while t:
                    while c < t.val and t.left:
                        t = t.left
                    while c > t.val and t.right:
                        t = t.right
                    if c < t.val and not t.left:
                        t.left = TreeNode(c)
                        break
                    if c > t.val and not t.right:
                        t.right = TreeNode(c)
                        break
        return root
