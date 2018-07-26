class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo=0
        hi=len(nums)-1
        if hi==0:
            return 0
        try:
            if nums[0]>nums[1]:
                return 0
            if nums[-1]>nums[-2]:
                return hi
            while(lo<=hi):
                mi=int((lo+hi)/2)
                if nums[mi-1]<nums[mi] and nums[mi]>nums[mi+1]:
                    return mi
                elif nums[mi-1]>nums[mi]:
                    hi=mi
                elif nums[mi]<nums[mi+1]:
                    lo=mi
        except:
            pass
