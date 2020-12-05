class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        maps = {}
        def dfs(node, depth):
            if node:
                if depth in maps:
                    if depth % 2 == 0:
                        maps[depth].append(node.val)
                    else:
                        maps[depth].insert(0, node.val)
                else:
                    maps[depth] = [node.val]

                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
        dfs(root, 0)
        return [v for k, v in maps.items()]
