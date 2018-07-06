class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        for item in itertools.permutations(nums):
            res.append(list(item))
        return res
