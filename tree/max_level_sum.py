import collections
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        self.maps = collections.defaultdict(list)
        
        def dfs(node, d):
            if node:
                self.maps[d].append(node.val)
                dfs(node.left, d+1)
                dfs(node.right, d+1)
                
        dfs(root, 1)
        
        ml,ms = 0, -math.inf
        for k,v in self.maps.items():
            s = sum(v)
            if s > ms:
                ms = s
                ml = k
        return ml  