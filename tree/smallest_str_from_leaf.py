class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return None
        self.smallest = ''

        def dfs(node, arr):
            if node:
                if not node.left and not node.right:
                    arr = [chr(97+node.val)]+arr
                    st = ''.join(arr)
                    if not self.smallest or st < self.smallest:
                        self.smallest = st
                    return
                dfs(node.left, [chr(97+node.val)]+arr)
                dfs(node.right, [chr(97+node.val)]+arr)

        dfs(root, [])
        return self.smallest
