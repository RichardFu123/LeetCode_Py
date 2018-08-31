# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) < 1: return None
        middle = int(len(nums) / 2)
        root = TreeNode(nums[middle])
        rt_root = root
        if middle-1 >= 0:
            root.left = self.sortedArrayToBST(nums[:middle])
        if middle+1 < len(nums):
            root.right = self.sortedArrayToBST(nums[middle+1: ])
            
        return rt_root
