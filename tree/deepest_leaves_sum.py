import collections
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        # bfs
        queue = [root]
        levels = []
        while queue:
            l,temp = len(queue), []
            while l > 0:
                curr = queue.pop(0)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                temp.append(curr.val)
                l-=1
            levels.append(temp)
            
        return sum(levels[-1])
        
        # dfs with hashmap
        
        # self.maps = collections.defaultdict(list)
        # def dfs(node, d):
        #     if node:
        #         self.maps[d].append(node.val)
        #         dfs(node.left, d+1)
        #         dfs(node.right, d+1)
        # dfs(root, 0)
        # m = max(self.maps.keys())
        # return sum(self.maps[m])