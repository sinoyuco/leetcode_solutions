class Solution:
    def constructTree(self, arr):
        if not arr:
            return None
        if len(arr) == 1:
            arr[0].left = None
            arr[0].right = None
            return arr[0]

        mid = (len(arr)-1)//2
        root = arr[mid]
        l, r = arr[:mid], arr[(mid+1):]
        root.left, root.right = self.constructTree(l), self.constructTree(r)
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = []

        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node)
                dfs(node.right)
        dfs(root)

        return self.constructTree(res)
