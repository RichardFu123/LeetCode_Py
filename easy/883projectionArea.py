class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        for i in grid:
            res+=max(i)
            for j in i:
                if j:
                    res+=1
        for k in zip(*grid):
            res+=max(k)
        return res
