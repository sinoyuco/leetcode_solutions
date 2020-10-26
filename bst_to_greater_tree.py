class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        result = 0

        def dfs(node):
            if node:
                # go to the highest valued node first,
                # add to result variable and set the new node value to the result.
                dfs(node.right)
                nonlocal result
                result += node.val
                node.val = result
                dfs(node.left)

        dfs(root)
        return root
