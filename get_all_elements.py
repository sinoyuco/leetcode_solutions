def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
      lst = []

       def dfs(node):
            if node:
                lst.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root1)
        dfs(root2)
        
        return sorted(lst)
