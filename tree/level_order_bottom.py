class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            l, temp = len(queue), []
            while l > 0:
                c = queue.pop(0)
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
                temp.append(c.val)
                l -= 1
            res.append(temp)
        return res[::-1]
