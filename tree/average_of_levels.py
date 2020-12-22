import collections


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        maps = collections.defaultdict(list)

        def dfs(node, depth):
            if not node:
                return
            maps[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return [sum(v)/len(v) for v in maps.values()]
