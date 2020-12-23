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

        # iterative 
        
        # if not root:
        #     return []
        # stack = [root]
        # while stack:
        #     curr = stack.pop()
        #     stack.extend(curr.children)
        #     res.append(curr.val)
        # return res[::-1]
