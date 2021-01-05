class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:

        queue = [(root, 1)]
        i = 0
        while i < len(queue):
            c, v = queue[i]
            i += 1
            if c:
                queue.append((c.left, 2*v))
                queue.append((c.right, 2*v+1))
        return queue[-1][-1] == len(queue)
