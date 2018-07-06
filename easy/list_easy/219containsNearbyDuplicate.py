class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = dict()
        for index,value in enumerate(nums):
            if value in dic and index - dic[value] <= k:
                return True
            dic[value] = index
        return False
