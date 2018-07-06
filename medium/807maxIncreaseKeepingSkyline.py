class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = list(zip(*grid))
        res=0
        for i in grid:
            for j in range(len(i)):
                res+=min(max(i),max(col[j]))-i[j]
                
        return res
