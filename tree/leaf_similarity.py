class Solution:
    def dfs(self, node,results):
        if node:
            self.dfs(node.left, results)
            if not node.left and not node.right:
                results.append(node.val)
            self.dfs(node.right, results)
        return results
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.dfs(root1,[]) == self.dfs(root2,[])