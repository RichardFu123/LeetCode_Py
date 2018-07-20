class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        if not nums or k==1:
            return nums
        deq=collections.deque(nums[:k],maxlen=k)
        res.append(max(deq))
        for i in nums[k:]:
            deq.append(i)
            res.append(max(deq))
        return res
        
