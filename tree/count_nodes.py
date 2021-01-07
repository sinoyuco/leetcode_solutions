class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        l,r = self.dfs(root.left), self.dfs(root.right)
        if l == r:
            return 2**l + self.countNodes(root.right)
        else:
            return 2**r + self.countNodes(root.left)
    
    def dfs(self, node):
            if not node:
                return 0
            return 1 + self.dfs(node.left)
        