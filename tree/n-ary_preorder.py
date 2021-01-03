class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            curr = queue.pop()
            if curr:
                res.append(curr.val)
                for c in curr.children[::-1]:
                    queue.append(c)
        return res
