class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=''
        s=[]
        for i in range(len(nums)):
            if nums[i]!=1:
                nums[i]=0
            a+=str(nums[i])
        s=str(a).split('0')
        count=0
        for S in s:
            if len(S)>count:
                count=len(S)
        return count
