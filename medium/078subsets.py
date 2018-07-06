class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        res.append([])
        for i in range(len(nums)+1):
            for item in itertools.combinations(nums,i):
                if list(item) not in res:
                    res.append(list(item))
        return res
