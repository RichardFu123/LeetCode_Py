class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if j == len(grid[0])-1 and i== len(grid)-1:
                    continue
                elif j == len(grid[0])-1:
                    grid[i][j] = grid[i+1][j] + grid[i][j]
                elif i == len(grid)-1:
                    grid[i][j] = grid[i][j] + grid[i][j+1]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i+1][j],grid[i][j+1])
        return grid[0][0]
