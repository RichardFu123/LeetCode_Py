'''
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i)>(len(nums)/2):
                return i
                break
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                cand, count = i, 1
            else:
                if i == cand:
                    count = count + 1
                else:
                    count = count - 1
        return cand
