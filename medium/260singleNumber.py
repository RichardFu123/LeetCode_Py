class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=collections.Counter(nums)
        return [c.most_common()[-1][0],c.most_common()[-2][0]]
