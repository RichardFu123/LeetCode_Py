class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c=collections.Counter(nums)
        res=[]
        for i in c.most_common(k):
            res.append(i[0])
        return res
