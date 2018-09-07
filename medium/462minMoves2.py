class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[int(len(nums) / 2)]
        return sum(abs(num - median) for num in nums)
