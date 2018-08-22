class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        for i in itertools.combinations(range(1,10),k):
            if sum(i)==n:
                res.append(i)
        return res
