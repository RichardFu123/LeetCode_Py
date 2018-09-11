class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        nums.sort(reverse = True)
        for i in range(n-2):
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] <= nums[i]:
                    k -= 1
                else:
                    count += k - j
                    j += 1
        return count
