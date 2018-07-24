class Solution(object):  
    def thirdMax(self, nums):  
        """ 
        :type nums: List[int] 
        :rtype: int 
        """  
        if len(nums)<3:  
            return max(nums) 
        nums.sort()  
        k=3  
        for i in range(len(nums)-1):  
            if nums[len(nums)-1-i]>nums[len(nums)-2-i]:  
                k-=1  
            if k==1:  
                break  
            if i==len(nums)-2:  
                return max(nums)  
        return nums[len(nums)-2-i]  
