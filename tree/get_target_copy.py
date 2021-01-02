class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        self.answer = None

        def dfs(node, clone):
            if node:
                if node.val == target.val:
                    self.answer = clone
                dfs(node.left, clone.left)
                dfs(node.right, clone.right)

        dfs(original, cloned)
        return self.answer
