class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            for c in node.children:
                dfs(c)
            res.append(node.val)
        dfs(root)
        return res
