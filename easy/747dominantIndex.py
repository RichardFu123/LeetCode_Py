class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f=0
        s=0
        flag=0
        for i in range(len(nums)):
            if nums[i]>f:
                s=f
                f=nums[i]        
                flag=i
            if nums[i]<f:
                s=max(s,nums[i])
        if f>=(s*2):
            return flag
        else:
            return -1
