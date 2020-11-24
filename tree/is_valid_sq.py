class Solution:
    def dfs(node,arr,i):
        if not node or node.val != arr[i]:
            return False
        if i == len(arr)-1 and node.val == arr[i] and not node.left and not node.right:
            return True
        return dfs(node.left, arr, i+1) or dfs(node.right, arr, i+1)

    def isValidSequence(root,arr):
        return dfs(root, arr, 0)