def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
      depth = {None: -1}

       def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        a = max(depth.values())

        def dfs2(node):
            if not node:
                return node

            if depth.get(node, None) == a:
                return node
            L, R = dfs2(node.left), dfs2(node.right)
            return node if L and R else L or R
        return dfs2(root)
