class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curSum=maxSum=0
        for i in range(1,len(prices)):
            curSum=max(0,curSum+prices[i]-prices[i-1])
            maxSum = max(curSum,maxSum)
        return maxSum
