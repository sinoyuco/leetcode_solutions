class Solution:
    def dfs(self, arr):
        if not arr:
            return [None]
        result = []
        for i in range(len(arr)):
            l,r = self.dfs(arr[:i]), self.dfs(arr[(i+1):])
            for lnode in l:
                for rnode in r:
                    root = TreeNode(arr[i])
                    root.left, root.right = lnode,rnode
                    result.append(root)
        return result
        
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        arr = [i+1 for i in range(n)]
        return self.dfs(arr)