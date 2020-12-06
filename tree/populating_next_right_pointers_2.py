class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = []
        if root:
            queue.append(root)

        while queue:

            temp = [n for node in queue for n in [node.left, node.right] if n]

            for i in range(len(temp)-1):
                temp[i].next = temp[i + 1]

            queue = temp

        return root
