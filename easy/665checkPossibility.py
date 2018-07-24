class Solution:
    def checkPossibility(self, nums):
        """
        time  : O(n)
        space : O(1)
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        counter = 0

        for i in range(1, l):
            if nums[i] < nums[i-1]:
                if i+1 < l and i-2 >= 0: 
                    f = nums[i+1] < nums[i-1]
                    s = nums[i-2] > nums[i]  
                    if s and f:
                        return False
                    else:
                        counter += 1
                        if counter > 1:
                            return False
                else:
                    counter += 1
                    if counter > 1:
                        return False
                    
        return True
