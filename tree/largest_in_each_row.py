class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        queue = [root]
        res = []
        #[[1], [3,2], [5,3,9]]
        while queue:
            l, temp = len(queue), []
            while l > 0:
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                temp.append(curr.val)
                l -= 1
            res.append(temp)
        return [max(i) for i in res]
