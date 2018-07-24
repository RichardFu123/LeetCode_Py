class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = [[0 for t in range(n)] for x in range(m)]
        count[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    count[i][j] = 1
                elif i == 0:
                    count[i][j] = count[i][j - 1]
                elif j == 0:
                    count[i][j] = count[i - 1][j]
                else:
                    count[i][j] = count[i - 1][j] + count[i][j - 1]
        return count[m - 1][n - 1]
