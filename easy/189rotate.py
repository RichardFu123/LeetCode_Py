class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        k=k%len(nums)
        a=[]
        b=[]
        a=nums[:-k]
        b=nums[-k:]
        b.extend(a)
        nums[:]=b
