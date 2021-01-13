class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        def dfs(node, parent):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)

        queue = [(target, 0)]
        seen = {target}

        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.pop(0)
            for neighbor in (node.left, node.right, node.parent):
                if neighbor and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, d+1))
        return []
