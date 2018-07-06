class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        ans = 1
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[j] > nums[j-1]:
                    ans = max(ans, j-i+1)
                    j += 1
                else:
                    break
                
            i = j
        return ans
