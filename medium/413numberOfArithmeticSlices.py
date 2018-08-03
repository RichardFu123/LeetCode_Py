class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        dp = [0, A[1] - A[0], 1]
        for i in range(2,len(A)):
            det = A[i] - A[i - 1]
            if det == dp[1]:
                dp[0] += dp[2]
                dp[2] += 1
            else:
                dp[1] = det
                dp[2] = 1
        return dp[0]
            
