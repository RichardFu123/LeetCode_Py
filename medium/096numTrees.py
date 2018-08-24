class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n+1)]
        for i in range(2,n+1):
            dp[i] = sum([dp[j-1] * dp[i-j] for j in range(1,i+1)])
        return dp[-1]
