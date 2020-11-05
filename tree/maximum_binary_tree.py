def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

    if not nums:
        return
    if len(nums) ==1:
        return TreeNode(nums[0])

    idx = nums.index(max(nums))
    left, right = nums[:idx], nums[idx+1:]
    node = TreeNode(nums[idx])

    node.left = self.constructMaximumBinaryTree(left)
    node.right = self.constructMaximumBinaryTree(right)

    return node
