import collections
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict(collections.Counter(nums))
        max = 0
        for i in dic:
            if dic.get(i,0) > 0 and dic.get(i+1,0) > 0 and dic.get(i,0)+dic.get(i+1,0) > max:
                max = dic.get(i,0) + dic.get(i+1,0)
        return max
