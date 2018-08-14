class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        mid = nums.index(max(nums))
        node = TreeNode(nums[mid])
        node.left = self.constructMaximumBinaryTree(nums[:mid])
        node.right = self.constructMaximumBinaryTree(nums[mid+1:])
        return node
