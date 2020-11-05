class Solution:
    def pre(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def suc(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        node = root
        if node.val == key:
            if not (node.right or node.left):
                node = None
            else:
                if node.right:
                    node.val = self.suc(node)  # 4
                    node.right = self.deleteNode(node.right, node.val)
                else:
                    node.val = self.pre(node)
                    node.left = self.deleteNode(node.left, node.val)
        elif key > node.val:
            node.right = self.deleteNode(node.right, key)
        else:
            node.left = self.deleteNode(node.left, key)
        return node
