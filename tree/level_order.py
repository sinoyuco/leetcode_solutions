class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            l, t = len(queue), []
            while l > 0:
                nextNode = queue.pop(0)

                if nextNode.left:
                    queue.append(nextNode.left)

                if nextNode.right:
                    queue.append(nextNode.right)

                t.append(nextNode.val)
                l -= 1
            result.append(t)
        return result
