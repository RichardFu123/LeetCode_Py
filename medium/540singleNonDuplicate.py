class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(int(len(nums)/2)):
            if nums[2*i]!=nums[2*i+1]:
                return nums[2*i]
        else:
            return nums[-1]


class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums) - 1
        low = 0
        high = l 
        while low <= high:
            mid = (low + high)//2
            if mid + 1 > high or mid - 1 < low:
                break
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    low = mid + 2
                else:
                    high = mid + 1
            else:
                if nums[mid] == nums[mid-1]:
                    low = mid + 1
                else:
                    high = mid
        return nums[mid]
