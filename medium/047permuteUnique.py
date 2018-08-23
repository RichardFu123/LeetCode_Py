class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resset=set()
        for i in itertools.permutations(nums):
            resset.add(i)
        return list(resset)
