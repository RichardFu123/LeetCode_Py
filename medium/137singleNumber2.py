class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=collections.Counter(nums)
        return c.most_common()[-1][0]
