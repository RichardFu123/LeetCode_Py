class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum = sum(nums[:])
        left_sum = 0
        pivot = -1
        
        for i in range(len(nums)):
            
            if(totalsum - nums[i] == left_sum):
                return i
            
            left_sum = left_sum + nums[i]
            
            totalsum = totalsum-nums[i]
            
            
        return pivot 
