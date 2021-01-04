import collections
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.maps = collections.defaultdict(int)
        
        def dfs(node):
            if node:
                self.maps[node.val] += 1
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        m = max(self.maps.values())
        arr = []
        for k,v in self.maps.items():
            if v == m:
                arr.append(k)
        return arr