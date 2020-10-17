class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        root_idx = len(nums)//2
        root = TreeNode(nums[root_idx])

        root.left = self.sortedArrayToBST(nums[:root_idx])
        root.right = self.sortedArrayToBST(nums[(root_idx+1):])

        return root
