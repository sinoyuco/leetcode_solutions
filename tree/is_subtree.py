class Solution:
    def same(self, n1, n2):
        if not n1 and not n2:
            return True
        if (not n1 and n2) or (n1 and not n2):
            return False
        if n1.val != n2.val:
            return False
        return self.same(n1.left, n2.left) and self.same(n1.right, n2.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False
        check = False
        if s.val == t.val:
            check = self.same(s, t)
        return check or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
