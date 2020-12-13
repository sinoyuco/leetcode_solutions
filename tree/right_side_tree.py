class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        maps = {}
        def dfs(node, depth):
            if node:
                if depth in maps:
                    maps[depth].append(node.val)
                else:
                    maps[depth] = [node.val]
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
        dfs(root, 0)
        return [l[-1] for l in maps.values()]
