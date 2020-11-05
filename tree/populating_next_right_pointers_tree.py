class Solution:
    def connect(self, root: 'Node') -> 'Node':
        maps = {}

        def dfs(node, depth):
            if not node:
                return
            if depth in maps:
                maps[depth][-1].next = node
                maps[depth].append(node)
            else:
                maps[depth] = [node]
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 1)
        return root
