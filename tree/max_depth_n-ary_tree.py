class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue, m = [root], 0
        while queue:
            m+=1
            for i in range(len(queue)):
                curr = queue.pop(0)
                for child in curr.children:
                    queue.append(child)
        return m