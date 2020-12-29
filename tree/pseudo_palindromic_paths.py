import collections
class Solution:
    def palindrome(self, array):
        maps = collections.Counter(array)
        found = False
        for v in maps.values():
            if v % 2 == 1:
                if found:
                    return False
                else:
                    found = True
        return True

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:

        self.res = 0
        def dfs(node, arr):
            if not node:
                return
            if not node.left and not node.right:
                print(arr+[node.val])
                if self.palindrome(arr+[node.val]):
                    self.res += 1
            dfs(node.left, arr + [node.val])
            dfs(node.right, arr + [node.val])

        dfs(root, [])
        return self.res
