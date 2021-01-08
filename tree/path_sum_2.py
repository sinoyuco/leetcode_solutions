class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        self.res = []
        
        def dfs(node,path, s):
            if not node:
                return
            if not node.left and not node.right and s+node.val == sum:
                self.res.append(path+[node.val])
                return
            dfs(node.left, path+[node.val], s+node.val)
            dfs(node.right, path+[node.val], s+node.val)
            
        dfs(root, [], 0)
        return self.res