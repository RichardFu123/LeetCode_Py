class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if nums is None or len(nums) == 0:
            return 0.0
        length = len(nums)
        if length <= k:
            return sum(nums) / length
        max_v, cur_v = sum(nums[:k]), sum(nums[:k])
        for i in range(k, length):
            pre_v = cur_v
            cur_v = pre_v + nums[i] - nums[i-k]
            if max_v < cur_v:
                max_v = cur_v
        return max_v / k
