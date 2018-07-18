class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        li=[]
        res=[]
        for i in range(1,n+1):
            li.append(i)
        for j in itertools.combinations(li,k):
            res.append(list(j))
        return res
