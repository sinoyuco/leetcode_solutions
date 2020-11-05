class Solution:
    def getmaxHeight(self, node):
           if not node:
                return 0
            return 1+max(self.getmaxHeight(node.left), self.getmaxHeight(node.right))

    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []
        size = self.getmaxHeight(root)
        result = [['' for i in range(2**size-1)] for j in range(size)]

        def dfs(node, h,i):
            if h ==0:
                return
            if node:
                result[size-h][i] = str(node.val)
                dfs(node.left, h-1, i-2**(h-2))
                dfs(node.right, h-1, i+2**(h-2))
        dfs(root, size, (2**size-1)//2)
        return result
