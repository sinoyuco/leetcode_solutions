class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        a = set()
        def dfs(node, res):
            if node:
                nonlocal a
                if not res:
                    res = str(node.val)
                else:
                    res = res + '->' + str(node.val)
                    
                if not node.left and not node.right:
                    a.add(res)
                    return
                dfs(node.left,res)
                dfs(node.right,res)
        dfs(root, '')
        return a