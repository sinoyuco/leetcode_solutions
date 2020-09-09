def sumRootToLeaf(self, root: TreeNode) -> int:

    def dfs(node):
        if (not node):
            return ''
        if not node.left and not node.right:
            return [str(node.val)]
        return [str(node.val) + i for i in dfs(node.left)] + [str(node.val) + i for i in dfs(node.right)]

    count = 0
    result = dfs(root)
    for i in range(len(result)):
        count += int(result[i], 2)

    return count
