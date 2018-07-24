class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum=maxSum=nums[0]
        for i in range(1,len(nums)):
            curSum = max(nums[i],curSum+nums[i])
            maxSum = max(curSum,maxSum)
        return maxSum
