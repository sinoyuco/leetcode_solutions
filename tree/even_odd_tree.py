class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        def checkNode(node, depth, prev):
            if not node:
                return True
            if (depth%2==0 and node.val%2==0) or (depth%2!=0 and node.val%2!=0):
                return False
            if depth in prev:
                if (depth%2==0 and prev[depth] >= node.val) or (depth%2!=0 and prev[depth] <= node.val):
                    return False
            prev[depth] = node.val
            return checkNode(node.left, depth+1, prev) and checkNode(node.right, depth+1, prev)
        return checkNode(root, 0, {})