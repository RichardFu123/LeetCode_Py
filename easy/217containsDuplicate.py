class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1=set(nums)
        if len(set1)<len(nums):
            return True
        else:
            return False
