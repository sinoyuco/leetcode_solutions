class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, left=root)

        def dfs(node, depth):
            if depth == 1:
                l, r = TreeNode(v, left=node.left), TreeNode(
                    v, right=node.right)
                node.left = l
                node.right = r
            if node.left:
                node.left = dfs(node.left, depth-1)
            if node.right:
                node.right = dfs(node.right, depth-1)
            return node
