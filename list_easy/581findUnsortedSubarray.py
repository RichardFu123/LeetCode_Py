class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_same = [a == b for (a, b) in zip(nums, sorted(nums))]
        return 0 if all(all_same) else len(nums) - all_same.index(False) - all_same[::-1].index(False)
