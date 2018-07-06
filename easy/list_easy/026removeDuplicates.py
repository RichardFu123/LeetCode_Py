class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=list(set(nums))
        a.sort()
        nums[:]=a
