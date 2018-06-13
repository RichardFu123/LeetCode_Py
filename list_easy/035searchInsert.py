class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag = 0
        for i in nums:
            if i == target or i >= target:
                return flag
                break
            
            flag+=1
        return flag
            
